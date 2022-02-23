import './App.css';
import { Button , Row } from 'react-bootstrap';


// get the product list from a restful api localhost:8000/product/product
// with user name and password admin/houssem
async function getProducts() {
  try {
    const response = await fetch('http://localhost:8000/product/product');
    const data = await response.json();
    return data.products;
  } catch (error) {
    return console.log(error);
  }
}

function ButtonDelete() {
    return (
        <button className="button-delete">Delete</button>
    )
}

// displays product name a delete button 
function Product(params) {
            return (
              <div>
                <Row className="mx-0">
                  <h1>{params.name}</h1> 
                  <ButtonDelete/>
                </Row>
              </div>
            )
}

// gets the product list from a restful api and displays it
function ProductList() {
  return (
      <div className="product-list">
          {getProducts().map(product => (
              <Product name={product.name}/>
          ))}
      </div>
  )
}

// beautiful header that stays on top no matter how much you scroll


// a simple product list
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Product list</h1>
      </header>
      <ProductList/> 

    </div>
  );
}

export default App;
