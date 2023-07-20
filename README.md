# Oven Temperatures Lab Part 2 Solution

## Overview
There are five main components to the solution:
1. Oven Temperature Reader: `oven/`
2. Kafka Zookeeper: `zookeeper/`
3. Kakfa Broker: `broker/`
4. Kafka Producer (Python): `kafka_producer/`
5. Kafka Consumer (Spark): `spark/`

In each respective directory is the associated `Dockerfile` used to build the docker image for each component.

## Steps
1. For each component, enter the directory and build the docker image. For example for the Kafka Zookeeper, you would:
```
$ cd zookeeper
$ docker build -t zookeeper:latest
```
The following steps must be taken in each `Dockerfile`:
* Oven REST API: follow the instructions [here](https://fastapi.tiangolo.com/deployment/docker/#dockerfile)
  * build from `python:3.9`
  * copy a `requirements.txt` file containing the required python libraries
  * copy the `main.py` file containing your REST API to the `/code/` container directory
  * run the `uvicorn` command to launch your API
* Zookeeper: use the [getting started guide](https://developer.confluent.io/get-started/python/#kafka-setup) for guidance (with kafka location set to `Local`)
  * build from `confluentinc/cp-zookeeper:7.3.0`
  * set environment variables
* Broker: use the [getting started guide](https://developer.confluent.io/get-started/python/#kafka-setup) for guidance (with kafka location set to `Local`)
  * build from `confluentinc/cp-kafka:7.3.0`
  * set environment variables
  * create a new topic called `oven`
* Zookeeper: provide students with the Dockerfile 
  * build from `confluentinc/cp-zookeeper:7.3.0`
* Spark (Kafka Consumer): provide students with the Dockerfile 
  * build from `jupyter/pyspark-notebook`
  * copy the required .jar files from the `jar/` directory
  * copy a `requirements.txt` file containing the required python libraries
  * run `pip install` using the copied `requirements.txt` file

Build using the jupyter/pyspark-notebook image from dockerhub
Have your container port set to forward 8888 to 10000
Set your working directory (containing your .ipynb file) to /home on your container
Kafka Zookeeper



**NOTE: Apple M1 Machines**: If you are using an Apple M1 laptop, update the first line in `kafka_producer/Dockerfile` from `FROM confluentinc/cp-kafka:latest` to
`FROM confluentinc/cp-kafka:latest.amd64`
2. In the root directory where the `docker-compose.yaml` file is located, bring the containers up by running:
```
$ docker compose up
```
3. Using either the docker dashboard or `docker exec`, view the `spark` container logs to find the jupyterlab link and grab the token:
```
$ docker exec spark "jupyter notebook list"
```
4. http://localhost:10000/API_TOKEN
5. Run the `demo.py` file in the root directory of your `spark` container to read temperature readings into a Spark DataFrame.
