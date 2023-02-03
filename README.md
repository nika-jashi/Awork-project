<H1>Awork Project</H1>
### Description

## Project requirements

* python >= 3.8
* Docker >= 20.10.18
``This is Case When you Don't Run Project localy
``

## Development Environment Set Up

### Start project directly on your host

#### Virtual Environment Set up

```bash
  python -m venv <path_to_env>
  source <path_to_env>/bin/activate
```
#### before running project don't forget to install all the requirement packages
```bash
    pip install -r requirments.txt
```
#### To Start Project Write This Command In Terminal

```bash
  flask run
```

```command 'flask run' will automaticaly create database with all necesery tables```

## In Case Of Using Dockerfile

### start project in virtual machine

#### to create image of the project
```bash
docker build -t <image-name> .
```
#### to run created image 
```bash
docker run -dp <port:port> <image-name>
```
``-d flag to run the new container in “detached” mode
``

``-p flag to create a mapping between the host’s port to the container’s port
``
#

### NOTE
* Currently, API is Only Usable Through Postman or Similar services
``(JWT authentication for this moment only works through it )
``