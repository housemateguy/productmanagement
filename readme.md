## Install requirment

pip install -r requirements.txt

## Run the backend (rest api)

python manage.py runserver

## API documentation

api root url: <http://localhost:8000/product/>

## Send API requests

Product type:

### post

curl -H "Content-Type: application/json" -u admin:houssem <http://localhost:8000/users/> -X POST -d '{"name": "Product Type 1", }' <http://localhost:8000/product/producttype/>

### get

curl -H "Content-Type: application/json" -u admin:houssem <http://localhost:8000/users/> -X GET <http://localhost:8000/product/producttype/>
