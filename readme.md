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


``` cd frontend/modifyproduct
npm start
```





