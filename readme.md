# BLE discovery

**TODO**
- [ ] the discovery files should run in background and restarted if crashed
- [ ] request the devices.json file 

**discovery.py**
the discovery.py file will request all bluetooth devices around every 3 seconds and write the mac adress and the signal strengh in the devices.json file

**app.py**
app.py is the flask server and will render the html page where the dataviz will happen

## Requirements
- Docker
- Docker-compose

## Easy Setup 
> docker-compose build
> docker-compose up

the server should be available on localhost:5000 :D

## Manual setup

**Requirements**
- Linux system (raspian and ubuntu have been tested and are working on this repo )
- Python 3 
- pip

**setup**
> pip3 install -r src/requirements.txt
> flask run

the server should be available on localhost:5000 :D