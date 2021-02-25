const PlaceDetail = ({place}) => {
  return (
    <div>
      <h2>{place.name}</h2>
      <a href={place.wikipedia}>More Information</a>
      <p><img src={`${place.image}`} height='100px' width='100px'/></p>
      <p>{place.extract}</p>
    </div>
  )
}

const DisplaySearchBar = (props) => {
  const [query, setQuery] = React.useState(null);
  const [places, setPlaces] = React.useState([]);
  const [display, setDisplay] = React.useState(false)
  console.log('beginning Search');
  console.log(places);

  const handleSearchInput = (evt) => {
    setQuery(evt.target.value);
    console.log('query:', query, 'places: ', places);

  }
  
  const handleSearch = (evt) => {
    evt.preventDefault();
    console.log('SEARCHING');
    
    const url = `/api/destination/search.json?places=${query}`;
    console.log(url);

    fetch(url) 
    .then((res) => res.json())
    .then((results) => {console.log('line 38', results); return results})
    .then((results) => setPlaces(results.places))
    .then(() => setDisplay(true));
    
    console.log(' before for loop places', places);
  
    };
    console.log(query, places);
    
    const generateSearchResults = () => {
    if (places.length === 0) return <div>Please Wait...</div>;
  
      const details = [];
      console.log('before line 46');
      for (const place of places) {
        details.push(<PlaceDetail place={place} key={name}/>);
      }
      return <div>{details}</div>
  }
  return (
    <div>
    <div className="nav-search">
      <div class="form-group mb-2">
        <form onSubmit={handleSearch} class="form-inline">
          <div class="form-group mx-sm-3 mb-2">
            <input 
                  type="search"
                  class="form-control"
                  placeholder="Where are you heading?" 
                  name="search_input" 
                  onChange={handleSearchInput} 
                  value={query}/>
            <button type="button" class="btn btn-primary"> Go </button>
          </div>
        </form>
      </div>
    </div>
    <div>{generateSearchResults()}</div>
    </div>
  )
}

