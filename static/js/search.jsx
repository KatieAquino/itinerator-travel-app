const PlaceDetail = (props) => {
  const { place } = props;
  return (
    <div>
      <h2>{place.name}</h2>
      <a href={place.wikipedia}>More Information</a>
      <p><img src={`${place.image}`} height='100px' width='100px'/></p>
      <p>{place.extract}</p>
    </div>
  )
}

const SearchBar = (props) => {
  const [query, setQuery] = React.useState(null);
  const [places, setPlaces] = React.useState({});
  console.log('beginning Search');

  // const initialSearchInput = Object.freeze({
  //   query: '',
  // });

  const handleSearchInput = (evt) => {
    setQuery(evt.target.value);
    //   ...query, [evt.target.name]: evt.target.value
    // })
  }
  
  const Search = (evt) => {
    evt.preventDefault();
    console.log('SEARCHING');
    
    const url = `/api/destination/search.json?places=${query}`;
    console.log(url);

    fetch(url) 
    .then((res) => res.json())
    .then((results) => {console.log(results); return results})
    .then((results) => setPlaces(results.places));
    
    // console.log('places', places);
    // if (places.length === 0) return <div>Please Wait...</div>;
    console.log(places);
    const details = [];
    for (const place of places) {
      details.push(<PlaceDetail name={place.name} 
                                wikipedia={place.wikipedia} 
                                image={place.image} 
                                extract={place.extract}/>);
    }
    return <div>{details}</div>
  
    };
    console.log(places);
  return (
    <div className="nav-search">
      <form onSubmit={Search}>
        <input type="search" placeholder="Where are you heading?" name="search_input" onChange={handleSearchInput} value={query}/>
        <button className="search-button" type="submit">Go</button>
      </form>
    </div>
  )
}