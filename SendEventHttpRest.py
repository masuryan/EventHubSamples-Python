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
    my_headers = {'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiJodHRwczovL2V2ZW50aHVicy5henVyZS5uZXQiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDcvIiwiaWF0IjoxNjI2MTA0MDk3LCJuYmYiOjE2MjYxMDQwOTcsImV4cCI6MTYyNjE5MDc5NywiYWlvIjoiRTJaZ1lNZ3QrbWUrUTFlVHJYbnF0NzBxSDU0OUJBQT0iLCJhcHBpZCI6Ijg3ZjBkOWQzLWE5YjItNDQ3YS05OGEzLWQ3Nzk5ZmYyMDdhMyIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzcyZjk4OGJmLTg2ZjEtNDFhZi05MWFiLTJkN2NkMDExZGI0Ny8iLCJvaWQiOiJlNWMyY2FhYS1hMDNhLTRmNGYtYTZkOS1hNzhhNGVlMWEyYzUiLCJyaCI6IjAuQVJvQXY0ajVjdkdHcjBHUnF5MTgwQkhiUjlQWjhJZXlxWHBFbUtQWGVaX3lCNk1hQUFBLiIsInN1YiI6ImU1YzJjYWFhLWEwM2EtNGY0Zi1hNmQ5LWE3OGE0ZWUxYTJjNSIsInRpZCI6IjcyZjk4OGJmLTg2ZjEtNDFhZi05MWFiLTJkN2NkMDExZGI0NyIsInV0aSI6IldtYy1VS2EtMEU2QWNMSWRJbmlvQUEiLCJ2ZXIiOiIxLjAifQ.J9dnhtgDrCw9eoXogL3qsQVRydDoGt3F8mBP3YXFNkNfcB9tb6yxRlAcT9ZMHQfA5121b4KdycVcfb-cIIPkbydU-QpRL6u8tfXfpaAZgAbfI9cOrTA8X73gdf8btpKCWeEk-uGrQ5lY7e11fKW-m00HNoQtbenJOhqMrfBIvaL90cCOESl2_mIvRA_qXYCSasp3p_eolqs9IbWwIrpYipnLaXG4BxGxnO0mjUJHSiYTnGJRmuhHtr33HKfOqhkx4NBVsdr3V4RoKsHYR5-MCUyHZPrSBMXIP6WJUr3npbRxLb3kFqsA5teq3DYbP4eN0cC1n9507DCUgFc0H9aXvg'}
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