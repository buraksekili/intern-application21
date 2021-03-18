Project assignment for Kartaca internship.

## Installation


```shell
$ git clone https://github.com/buraksekili/kartaca-service.git
```

## Usage


```shell
$ cd kartaca-service/
$ docker-compose up -d
$ curl localhost:4444/staj
Hello World from Flask!
 
$ curl localhost:5555/staj
Hello World from Node.JS!
 
$ curl localhost:8888/flask
Hello World from Flask!
 
$ curl localhost:8888/nodejs
Hello World from Node.JS!
```

### Caveat

If you are using Docker Desktop. `docker-compose` should be pre-installed on your setup. Otherwise (for Linux users), you need to install it. Check [this link](https://docs.docker.com/compose/install/) for installation