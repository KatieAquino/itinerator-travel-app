//Shortens ReactRouter objects for ease of use
const Route = ReactRouterDOM.Route;
const Link = ReactRouterDOM.Link;
const Switch = ReactRouterDOM.Switch;
const Router = ReactRouterDOM.BrowserRouter;

const Homepage = (props) => {
  return (
    <div>
      <h1>Welcome</h1>
      <h2>Plan Your Next Adventure</h2>
    </div>
  );
}

const Login = (props) => {
  return (
    <section>
      Returning User
        <p>
          <Link to="/login-user">
            <button className="user-button">Login</button>
          </Link>
        </p>
    </section>
  );
}

const NewUser = (props) => {
  return (
    <section>
      New User
        <p>
          <Link to="/create-account">
            <button className="user-button">Create Account</button>
          </Link>
        </p>
    </section>
  );
}

const TravelApp = (props) => {
  
  return (
    <Router>
      <div>
        <nav>
          <Link to="/">Home</Link>
          <div className="nav-search">
            <input type="text" placeholder="Where are you heading?" name="search" />
          </div>
        </nav>
        <Switch>
          <Route exact path="/">
            <Homepage />
            <Login />
            <NewUser />
          </Route>
          <Route path="/login-user">
            <UserLogin />
          </Route>
          <Route path="/create-account">
            <CreateAccount />
          </Route>
        </Switch>

      </div>
    </Router>
  );
}

ReactDOM.render(
  <TravelApp />,
  document.querySelector('#root')
);