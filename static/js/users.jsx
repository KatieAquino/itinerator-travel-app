const UserLogin = (props) => {

  return (
    <div class="container">
    <form action="/api/login-user" method="POST">
      <h2>Login</h2>
      <div class="form-group row">
        <label for="login-email" class="col-sm-2 col-form-label">Email:</label>
        <div class="col-sm-10">
          <input type="email" class="form-control" id="login-email" 
          name="login-email" required/>
        </div>
      </div>
      <div class="form-group row">
        <label for="login-password" class="col-sm-2 col-form-label">Password:</label> 
        <div class="col-sm-10">
        <input type="password" class="form-control" id="login-password" 
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
    <div class="container">
      <form action="/api/create-account" method="POST">
        <h2>Sign Up</h2>
        <div class="form-group row">
          <label for="new-username" class="col-sm-2 col-form-label">Username: </label>
          <div class="col-sm-10"> 
            <input 
                type="text" 
                class="form-control"
                id="new-username"
                name="new-username" 
                required/>
          </div>
          </div>
          <div class="form-group row">
          <label for="new-email" class="col-sm-2 col-form-label">Email: </label>
          <div class="col-sm-10"> 
            <input 
                type="text" 
                class="form-control"
                id="new-email"
                name="new-email" 
                required/>
          </div>
          </div>
          <div class="form-group row">
          <label for="new-password" class="col-sm-2 col-form-label">Password: </label>
          <div class="col-sm-10"> 
            <input 
                type="text" 
                class="form-control"
                id="new-password"
                name="new-password" 
                required/>
          </div>
          </div>
          <div class="form-group row">
          <label for="new-fname" class="col-sm-2 col-form-label">First Name: </label>
          <div class="col-sm-10"> 
            <input 
                type="text" 
                class="form-control"
                id="new-fname"
                name="new-fname" 
                required/>
          </div>
          </div>
          <div class="form-group row">
          <label for="new-lname" class="col-sm-2 col-form-label">Last Name: </label>
          <div class="col-sm-10"> 
            <input 
                type="text" 
                class="form-control"
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