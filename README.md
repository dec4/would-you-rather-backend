(in progress)

## About the Project

This is an implementation of the data store used in the Udacity reactnd Would You Rather project (TOOO: link).

Early stages of this app were made possible by following this tutorial: [Introduction to FastAPI and Local DynamoDB](https://medium.com/nerd-for-tech/introduction-to-fastapi-and-local-dynamodb-595c990ed0f8). Much thanks!

## Getting Started

### Prerequisites:

Ensure you have `python3.10`, `docker`, and `docker-compose` installed. This project also uses [dynamodb-admin](https://www.npmjs.com/package/dynamodb-admin) for easy access to the tables. You will need `npm>=12`.

`npm install -g dynamodb-admin`

### Installation/Setup:

`source venv/bin/activate`

### Usage:

There are three services defined in the `docker-compose.yml` file. The main app, the DynamoDB database, and dynamodb-admin.

1. Run `docker-compose up` to start all three containers.
1. Run `python3 local/init_db.py` to create the tables wyr-users and wyr-questions. This is required before using the main application. (TODO: work into docker steps to run automatically on container start)
