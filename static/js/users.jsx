const UserLogin = (props) => {

  return (
    <form action="/api/login-user" method="POST">
      <h2>Login</h2>
      <p>Email
        <input type="text" name="login-email" required/>
      </p>
      <p>
        Password
        <input type="password" name="login-password" required/>
      </p>
      <button className="user-button">Submit</button>
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