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

const CarouselHome = (props) =>{
  var Carousel = ReactBootstrap.Carousel
  return (
    <Carousel>
      <Carousel.Item interval={1000}>
        <img  className="d-block w-100"
              src={"static/images/shibuya-crossing.JPG"}
              alt="Shibuya crossing in Tokyo, Japan during the rain." />
      </Carousel.Item>
      <Carousel.Item interval={1000}>
        <img  className="d-block w-100"
              src="static/images/Schladming-Austria.JPG"
              alt="A view of the Dachstein mountain range from Schladming, Austria" />
      </Carousel.Item>
      <Carousel.Item interval={1000}>
        <img  className="d-block w-100"
              src="static/images/twelve-apostles.JPG"
              alt="The Twelve Apostles in the Pacific Ocean near Victoria, Australia." />
      </Carousel.Item>
      <Carousel.Item interval={1000}>
        <img  className="d-block w-100"
              src="static/images/grand-central-terminal.JPG"
              alt="A clock in Grand Central Terminal in New York City." />
      </Carousel.Item>
    </Carousel>
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
        <Switch>
          <Route exact path="/">
            <Homepage />
            <CarouselHome />
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