import time
import asyncio
import os

from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub.exceptions import EventHubError
from azure.eventhub import EventData


producer = EventHubProducerClient.from_connection_string(
        conn_str='Endpoint=sb://udaandemo.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=pXQyvZw2xvmrf79pbDPWGqO008gXbZ44e9QuP8gu2aM=',
        eventhub_name='testevents'
    )

async def send_event_data_batch(producer, msg):
    # Without specifying partition_id or partition_key
    # the events will be distributed to available partitions via round-robin.
    print("Sending the data")
    event_data_batch = await producer.create_batch()
    event_data_batch.add(EventData('message ASYNC 1' + msg))
    event_data_batch.add(EventData('message ASYNC 2' +  msg))
    event_data_batch.add(EventData('message ASYNC 3' + msg))
    await producer.send_batch(event_data_batch)


async def main():


    async with producer:
        await send_event_data_batch(producer,'batch1')
        time.sleep(20)
        await send_event_data_batch(producer,'batch2')




loop = asyncio.get_event_loop()
start_time = time.time()
loop.run_until_complete(main())
print("Send messages in {} seconds.".format(time.time() - start_time))