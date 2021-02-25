const UserLogin = (props) => {

  // const [username, setUsername] = useState('');
  // const [password, setPassword] = useState('');
  // const [user, setUser] = useState('');

  // const handleSubmit = async evt => {
  //   evt.preventDefault();

  // //   const user = { username, password };
  // //   const
  // // }
  // // if (user) {
  // //   return <div>Hi {user.name}!</div>
  // }
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
    <form action="/api/create-account" method="POST">
      <h2>Sign Up</h2>
      <p>Username
        <input type="text" name="new-username" required/>
      </p>
      <p>Email
        <input type="text" name="new-email" required/>
      </p>
      <p>Password
        <input type="password" name="new-password" required/>
      </p>
      <p>First Name
        <input type="text" name="new-fname"/>
      </p>
      <p>Last Name
        <input type="text" name="new-lname"/>
      </p>
      <button className="user-button">Submit</button>
    </form>
  );
}