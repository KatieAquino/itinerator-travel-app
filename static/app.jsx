const Login = (props) => {
  return (
    <section>
      Returning User
    </section>
  );
}

const NewUser = (props) => {
  return (
    <section>
      New User
    </section>
  );
}

const TravelApp = (props) => {
  
  return (
    <div>
      <Login/>
      <NewUser/>
    </div>
  );
}

ReactDOM.render(
  <TravelApp />,
  document.querySelector('#root')
);