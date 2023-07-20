import os
from time import sleep
import socket
import json

import requests
from confluent_kafka import Producer

CLIENT_ID = socket.getfqdn()
BOOTSTRAP_SERVERS = os.environ.get('KAFKA_BROKER')
REQUEST_URL = "http://oven:80"
KAFKA_TOPIC = 'oven'

def produce_to_kafka(topic, key=None, value=None):
    conf = {'bootstrap.servers': BOOTSTRAP_SERVERS,
            'client.id': CLIENT_ID
            }
    
    if value:
        value = json.dumps(value)\
                    .encode('utf-8')
    
    producer = Producer(conf)
    producer.poll(1)
    producer.produce(topic=topic,
                     key=key,
                     value=value
                    )
    
    producer.flush()

def get_temperature():
    r = requests.get(REQUEST_URL)\
                .json()["temperature"]
    
    return r


def main():
    while True:
        produce_to_kafka(topic=KAFKA_TOPIC,
                        key="temperature",
                        value=get_temperature()
                        )
        
        sleep(.5)

if __name__ == "__main__":
    main()