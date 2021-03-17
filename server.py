"""Server for Travel App"""

from flask import Flask, jsonify, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
import APIfunctions
import os
from jinja2 import StrictUndefined


app = Flask(__name__)

SECRET_KEY = os.environ['SECRET_KEY']
app.secret_key = SECRET_KEY


@app.route('/')
def display_homepage():
    """Show the homepage"""

    return render_template('index.html')


@app.route('/api/login-user', methods=['POST'])
def log_in_user():
    """Log in user"""

    email = request.form.get('login-email')
    password = request.form.get('login-password')

    user = crud.find_user_by_email(email)
    user_password = user.check_password(password)

    #verifies that user email and password match what is in database
    if user.email == email and user_password == True:
        session['user'] = user.id
        session['username'] = user.username
        flash('Successfully logged in!')
        
        return redirect('/profile')
    
    else:
        flash('Unable to login, please try again')

        return redirect('/')


@app.route('/api/create-account', methods=['POST'])
def create_account():
    """Create a new account"""

    username = request.form.get('new-username')
    email = request.form.get('new-email')
    password = request.form.get('new-password')
    fname = request.form.get('new-fname')
    lname = request.form.get('new-lname')

    #checks if user is already in database
    user = crud.find_user_by_email(email)
    
    #if user not already in database, create new user
    if user == None:
        user = crud.create_user(username, email, password, fname, lname)
        session['user'] = user.id
        session['username'] = user.username

        flash('Successfully created account and logged in.')

        return redirect('/profile')
    
    else:
        flash('Unable to create account with that email.')
        
        return redirect('/')


@app.route('/api/destination/search')
def show_user_places():
    """Display places for searched destination"""

    place = request.args.get('search_input')
    place = place.title()
    
    user = session['user']
    itineraries = crud.find_itinerary_by_user_id(user)

    place_found = crud.find_location_by_name(place)
    print(place_found)
    print('*********')

    if place_found != None:
        ('***** PLACE FOUND')
        poi_details = []
        details = crud.get_place_details(place_found)
        print(details)
        
        for detail in details:
            poi_details.append({'xid': detail.xid,
                                'name': detail.name,
                                'wikipedia': detail.wikipedia,
                                'image': detail.image,
                                'extract': detail.extract})
        

    else:
        ('********* going to get coordinates')
        location_coord = APIfunctions.get_place_coordinates(place)
        ('coordinates received')
        location = crud.create_location(place)
        poi_options = APIfunctions.get_points_of_interests(location_coord)
        ('list of places retrieved')
        poi_details = APIfunctions.get_place_info(poi_options)
        ('details retrieved')

        for poi in poi_details:
            xid = poi['xid']
            name = poi['name']
            wikipedia = poi['wikipedia']
            image = poi['image']
            extract = poi['extract']

            crud.create_place(wikipedia, xid, name, image, extract, location.id)

    # return jsonify({'places': poi_details})
    return render_template('search_results.html', 
                            poi_details=poi_details,
                            place=place,
                            itineraries=itineraries)


@app.route('/profile')
def show_user_profile():
    """Get User Itineraries & Entries"""

    if 'user' in session:
        print(session['user'])
        print('*' * 25)

        user = session['user']
        
        itineraries = crud.find_itinerary_by_user_id(user)
        username = session['username']

        print('*' * 100)
        print('user id', session['user'])
        print(itineraries)

        return render_template('profile.html', 
                                itineraries=itineraries,
                                username=username)
    
    else:
        flash('Please login')
        return redirect('/')


@app.route('/itinerary/<id>')
def show_entries_for_itinerary(id):
    """Display entries for itinerary"""

    entry_details = crud.find_entries_by_itinerary(id)
    itinerary = crud.find_itinerary_by_id(id)

    return render_template('itinerary_details.html',
                            entry_details=entry_details,
                            itinerary=itinerary)


@app.route('/api/create-itinerary', methods=['POST'])
def user_create_itinerary():
    """Allows user to create a new itinerary"""

    user = session['user']
    name = request.form.get('new-name')
    start_date = request.form.get('start-date')
    end_date = request.form.get('end-date')

    print('*' * 25)
    print('start_date: ', start_date)

    crud.create_itinerary(user, name, start_date, end_date)

    return redirect('/profile')


@app.route('/api/delete-itinerary/<id>', methods=['POST'])
def user_delete_itinerary(id):
    """Allows user to delete an itinerary."""

    itinerary = crud.find_itinerary_by_id(id)
    crud.delete_itinerary(itinerary)

    flash(f'Successfully deleted your itinerary.')
    return redirect('/profile')


@app.route('/api/edit-itinerary', methods=['POST'])
def user_edit_itinerary():
    """Allows user to edit an itinerary."""

    itinerary_id = request.form.get('itinerary-id')
    name = request.form.get('edit-name')
    start_date = request.form.get('edit-start-date')
    end_date = request.form.get('edit-end-date')

    print(name)
    print('*' * 100)
    print(itinerary_id)

    itinerary = crud.find_itinerary_by_id(itinerary_id)
    print(itinerary)

    crud.update_itinerary(itinerary, name, start_date, end_date)

    return redirect('/profile')


@app.route('/api/update-entry/<id>', methods=['POST'])
def user_edit_entry(id):
    """Allows user to edit an entry on an itinerary"""
    
    name = request.form.get('name-edit')
    comments = request.form.get('comment-edit')
    url = request.form.get('url-edit')
    entry = crud.find_entry_by_id(id)
    
    print('*' * 25)
    print('entry is: ', entry)
    print('*' * 25)

    crud.update_entry(name, comments, url, entry)

    flash(f'{name} successfully updated!')
    return redirect(f'/itinerary/{entry.itinerary_id}')


@app.route('/api/delete-entry/<id>', methods=['POST'])
def user_delete_entry(id):
    """Allows user to delete an entry from an itinerary."""


    entry = crud.find_entry_by_id(id)
    itinerary_id = entry.itinerary_id
    crud.delete_entry(entry)

    flash(f'Successfully updated your itinerary.')

    return redirect(f'/itinerary/{itinerary_id}')

@app.route('/api/new-entry', methods=['POST'])
def user_add_entry():
    """Allows user to add a new entry to an existing itinerary."""

    name = request.form.get('new-name')
    description = request.form.get('description')
    url = request.form.get('new-url')
    image = request.form.get('image-url')
    comment = request.form.get('add-comment')
    location = request.form.get('new-location')
    trip_day = request.form.get('trip-day')
    itinerary_id = request.form.get('itinerary-id')

    print(itinerary_id)
    print('*' * 100)
    crud.create_entry(  int(itinerary_id),
                        name,
                        description,
                        url,
                        image,
                        comment,
                        location,
                        trip_day,)

    return redirect(f'/itinerary/{itinerary_id}')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', port='5757', debug=True)