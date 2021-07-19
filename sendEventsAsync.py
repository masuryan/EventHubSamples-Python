import time
import asyncio
import os

from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub.exceptions import EventHubError
from azure.eventhub import EventData



async def async_send(str):
    """
    Send Event Async

    """
    producer = EventHubProducerClient.from_connection_string(
        conn_str='Endpoint=sb://udaandemo.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=pXQyvZw2xvmrf79pbDPWGqO008gXbZ44e9QuP8gu2aM=',
        eventhub_name='testevents'
    )
    async with producer:
        ids = await producer.get_partition_ids()
        print(ids)
        event_data_batch = await producer.create_batch()
        event_data_batch.add(EventData(str))
        await producer.send_batch(event_data_batch)

asyncio.run(async_send("test 12"))
time.sleep(20)
asyncio.run(async_send("test 22"))

