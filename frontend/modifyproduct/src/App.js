import React from "react";
import './App.css';
import { Button } from 'react-bootstrap';


class App extends React.Component {

	// Constructor
	constructor(props) {
		super(props);
		this.state = {
			items: [],
			DataisLoaded: false
		};
	}

	// ComponentDidMount is used to
	// execute the code
	componentDidMount() {
    // fetch loop
    for (let i = 0; i < 10; i++) {
      fetch('http://127.0.0.1:8000/product/product/'+ i +'/?format=json')
        .then(response => response.json())
        .then(json => {
          this.setState({
            items: this.state.items.concat(json)
          });
        });
    }
    // set state
    this.setState({
      DataisLoaded: true
    });
  } 
  // render and return table
  render() {
    if (this.state.DataisLoaded) {
      return (
        <div className="App">
          <table className="table table-striped">
            <thead>
              <tr>
                <th>Product name</th>
                <th>Product Id</th>
                <th>Type</th>
                <th>Update</th>
              </tr>
            </thead>
            <tbody>
              {this.state.items.map(item => (
                <tr key={item.id}>
                  <td>{item.name}</td>
                  <td>{item.id}</td>
                  <td>{item.pruduct_type}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      );
    } else {
      return <div>Loading...</div>;
    }

  }
}




export default App;
