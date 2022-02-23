## Install requirment

pip install -r requirements.txt

## Run the backend (rest api)

python manage.py runserver

## API documentation

api root url: <http://localhost:8000/product/>

(You can explore the api via the link above, login as username:admin/password:houssem needed)


## Send API requests

Product type:

### post

```curl -X POST -H "Content-Type: application/json" -d '{"name":"test"}' http://localhost:8000/product/product/```

### get

```curl -X POST -H "Content-Type: application/json" -d '{"name":"test"}' http://localhost:8000/product/product/```


## Run the frontend (rest api)

make sure the backend is running before you run the front or the products will not show up


``` cd frontend/modifyproduct
npm start
```


### Part Three

ideally there should be a form of authentification to view, modify or add products




