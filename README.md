# Falcon-celery

A Falcon server using Celery to manage tasks. The server has following routes:
- POST /fibonacci: Calculate the n th fibonacci number, append the result in the format task_id - result to data.txt file and store the task in MongoDB. Return the task's id in response.
- GET /fibonacci/:id: Find the task with corresponding id in data.txt and return the task's result in response.
- GET /login: Return JWT token if credentials are correct.
- POST /signup: Create a new account. 

Features:
- JWT authentication on every route except login and signup.
- Task management using Celery.
- Login with email and password.
- Signup with email and password.

## Usage

- Clone this repo.
- Install all necessary packages:

```bash
pipenv install
```

- Start waitress server:

```bash
pipenv shell
hupper -m waitress --port=8000 app:api
```

- Start the local mongoDB server:

```bash
mongod --dbpath YOUR_DB_PATH
```

- Start RabbitMQ server:

```bash
rabbitmq-service stop
rabbitmq-server
```

- Start the Celery server:

```bash
pipenv shell
hupper -m celery -A controller.tasks worker --loglevel=INFO --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)