# Lemon Orders
This project is a simple backend service that creates stock orders built with `Python` and `FastAPI`


## Getting Started

These instructions will get you a copy of the app up and running on your local machine for development and testing purposes.

### Prerequisites

Things you need to install the software and how to install them
- Ensure you have `Docker` installed on your local machine
- You can check if `Docker Compose` was installed on your machine like so 

```
docker-compose --version
```

### Installing

This is a step by step series of examples to get the project up and running on your local machine

First thing to do is clone the github repository like so

```
git clone https://github.com/johnchuks/lemon-orders.git
```

After cloning the repository, we will need to enter the current directory of the project with this command

```
cd lemon-orders
```

To build and run the container, we use this command below

```
docker-compose up --build
```

Finally we can go to `http://0.0.0.0:6500/docs` to communicate with our web server.

To bring down all running containers and network, Run `docker-compose down`.
