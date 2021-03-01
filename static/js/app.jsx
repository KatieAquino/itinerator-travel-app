//Shortens ReactRouter objects for ease of use
const Route = ReactRouterDOM.Route;
const Link = ReactRouterDOM.Link;
const Switch = ReactRouterDOM.Switch;
const Router = ReactRouterDOM.BrowserRouter;

//Displays homepage
const Homepage = (props) => {
  return (
    <div>
      <h1>Welcome</h1>
      <h2>Plan Your Next Adventure</h2>
    </div>
  );
}

const NavBar = (props) => {
  return (
    <div>
      <Link to="/">Home</Link>
      <div className="nav-search">
      <div className="form-group mb-2">
        <form action="/api/destination/search" className="form-inline">
          <div className="form-group mx-sm-3 mb-2">
            <input 
                  type="search"
                  className="form-control"
                  placeholder="Where are you heading?" 
                  name="search_input"  />
            <button type="button" className="btn btn-primary"> Go </button>
          </div>
        </form>
      </div>
    </div>
    </div>
  );
}

const Login = (props) => {
  return (
    <section>
      Returning User
        <p>
          <Link to="/login-user">
            <button type="button" className="btn btn-primary">Login</button>
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
            <button type="button" className="btn btn-primary">Create Account</button>
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
            <NavBar />
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