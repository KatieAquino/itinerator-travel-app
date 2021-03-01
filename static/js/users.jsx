const UserLogin = (props) => {

  return (
    <div className="container">
    <form action="/api/login-user" method="POST">
      <h2>Login</h2>
      <div className="form-group row">
        <label for="login-email" className="col-sm-2 col-form-label">Email:</label>
        <div className="col-sm-10">
          <input type="email" className="form-control" id="login-email" 
          name="login-email" required/>
        </div>
      </div>
      <div className="form-group row">
        <label for="login-password" className="col-sm-2 col-form-label">Password:</label> 
        <div className="col-sm-10">
        <input type="password" className="form-control" id="login-password" 
        name="login-password" required/>
        </div>
      </div>
      <button type="submit" className="btn btn-primary">Submit</button>
    </form>
    </div>
  );
}

const CreateAccount = (props) => {
  return (
    <div className="container">
      <form action="/api/create-account" method="POST">
        <h2>Sign Up</h2>
        <div className="form-group row">
          <label for="new-username" class="col-sm-2 col-form-label">Username: </label>
          <div className="col-sm-10"> 
            <input 
                type="text" 
                className="form-control"
                id="new-username"
                name="new-username" 
                required/>
          </div>
          </div>
          <div className="form-group row">
          <label for="new-email" className="col-sm-2 col-form-label">Email: </label>
          <div className="col-sm-10"> 
            <input 
                type="text" 
                className="form-control"
                id="new-email"
                name="new-email" 
                required/>
          </div>
          </div>
          <div className="form-group row">
          <label for="new-password" className="col-sm-2 col-form-label">Password: </label>
          <div className="col-sm-10"> 
            <input 
                type="text" 
                className="form-control"
                id="new-password"
                name="new-password" 
                required/>
          </div>
          </div>
          <div className="form-group row">
          <label for="new-fname" className="col-sm-2 col-form-label">First Name: </label>
          <div className="col-sm-10"> 
            <input 
                type="text" 
                className="form-control"
                id="new-fname"
                name="new-fname" 
                required/>
          </div>
          </div>
          <div className="form-group row">
          <label for="new-lname" className="col-sm-2 col-form-label">Last Name: </label>
          <div className="col-sm-10"> 
            <input 
                type="text" 
                className="form-control"
                id="new-lname"
                name="new-lname" 
                required/>
          </div>
          </div>
          <button type="submit" className="btn btn-primary">Submit</button>
      </form>
    </div>
  );
}