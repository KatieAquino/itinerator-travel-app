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
        <Login/>
        <NewUser/>
    </div>
  );
}

const Login = (props) => {
  return (
    <section>
      Returning User
        <p>
          <button className="user-button">Login</button>
        </p>
    </section>
  );
}

const NewUser = (props) => {
  return (
    <section>
      New User
        <p>
          <button className="user-button">Create Account</button>
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
          <div class="nav-search">
            <input type="text" placeholder="Where are you heading?" name="search" />
          </div>
        </nav>
        
        <Switch>
          <Route path="/">
            <Homepage />
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