import uuid
import datetime
import random
import json
import sys
import logging
import datetime
import time
import os

from azure.eventhub import EventHubClient, Sender, EventData


# Config this with your Azure EventHub parameters
ADDRESS = "amqps://************.servicebus.windows.net/**********"
# Event Hub SAS name
USER = "*******"
KEY = "*************************"

try:
    if not ADDRESS:
        raise ValueError("No EventHubs URL supplied.")

    # Create Event Hubs client
    client = EventHubClient(ADDRESS, debug=False, username=USER, password=KEY)
    #devicenumber = str(random.randint(1,3))
    #sender = client.add_sender(partition=devicenumber)
    sender = client.add_sender(partition="0")
    client.run()
    
    try:
        start_time = time.time()
        devices = []
        for x in range(0, 10):
         devices.append(str(uuid.uuid4()))

        for y in range(0,100000):
          for dev in devices:
            reading = {'source': 'python-code-caio-sensor' + str(random.randint(1,3)), 'id': dev, 'timestamp': str(datetime.datetime.utcnow()), 'uv': random.random(), 'temperature': random.randint(70, 100), 'humidity': random.randint(70, 100), 'motion': random.randint(0,1)}
            
            message = json.dumps(reading)
            
            #message = "Message {}".format(i)
            print("Sending Message" + message)
            sender.send(EventData(message))
    except:
        raise

except KeyboardInterrupt:
    pass
