# object_detection

### Prerequisite
 1. Please Install and run rabbitmq
 2. update the .env file and update the rabbitmq variables, eg host, port etc
 
## Running the api project

``` 
$ cd app
$ uvicorn main:app --reload
```

## Running the consumer
Stay in the root project directory i.e `object_detection` folder
```
$ python -m app.app.py
```

## Running the tests
Just run following command
```
$ pytest
```
