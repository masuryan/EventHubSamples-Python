import requests

import time
import asyncio
import os

# This module uses HTTP 1.1 REST API CALL instead of AMQP(used by SDK) .
# No limitations on Connections (because HTTP is session less )
# You can send Batch of Events also
# Access Token is Hardcoded, you can use SAS token also
# This can be called from any part of the code or you can make this a library
# for Batch of Events refer this: https://docs.microsoft.com/en-us/rest/api/eventhub/send-batch-events
async def sendEvents(query):
    my_headers = {'Authorization' : 'Bearer ACCESS TOKEN GENERATED}
    response = requests.post('https://udaandemo.servicebus.windows.net/testevents/messages', data = query, headers=my_headers)
    return  response

#Main Function
query2 = {'lat':'45', 'lon':'180'}
query1 = {'lat':'55', 'lon':'190'}
loop = asyncio.get_event_loop()
start_time = time.time()

response = loop.run_until_complete(sendEvents(query1))
print(response)
time.sleep(10)
response = loop.run_until_complete(sendEvents(query2))
print(response)

loop.close()
