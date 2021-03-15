'use strict';

$('#new-itinerary').click(function(){
    $('#itinerary-form').toggle('slow');
});

$('#edit-itinerary').click(function(){
    $('#edit-form').toggle('slow');
});

$('#add-entry').click(function () {
    $('#new-entry-form').toggle('slow', function(){

    });
});

$('#submit-entry').on('submit'), (evt) => {
    evt.preventDefault();

    const entryData = $('#entry-form').serialize();
    const url = '/api/new-entry'
    console.log(entryData)
    $.post(url, entryData, (res) => {

    });

    window.location.reload();
}

$('#delete-entry').on('click', (evt) => {
    evt.preventDefault();

    const deleteEntryInfo = {
        id: $('#delete-confirmed').val()
    };

    console.log(deleteEntryInfo)
    console.log(`/api/delete-entry/${deleteEntryInfo['id']}`)

    $.post(`/api/delete-entry/${deleteEntryInfo['id']}`, deleteEntryInfo, (res) => {

    });

    window.location.replace('/profile')
});

$('#delete-itinerary-confirmed').on('click', (evt) => {
    evt.preventDefault();
    console.log('delete button clicked')
    const deleteItinerary = {
        id: $('#delete-itinerary-id').val()
    };
    let url = (`/api/delete-itinerary/${deleteItinerary['id']}`);
    console.log(deleteItinerary);

    $.post(url, deleteItinerary, (res) => {

    });
    
    window.location.replace('/profile')
})