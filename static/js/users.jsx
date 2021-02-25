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
    <form action="/api/login-user" method="POST">
      <h2>Login</h2>
      <div class="form-group">
        <label for="login-email">Email</label> 
        <input type="email" class="form-control" id="login-email" 
        name="login-email" required/>
      </div>
      <div class="form-group">
        <label for="login-password">Password</label> 
        <input type="password" class="form-control" id="login-password" 
        name="login-password" required/>
      </div>
      <button type="submit" className="btn btn-primary">Submit</button>
    </form>
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