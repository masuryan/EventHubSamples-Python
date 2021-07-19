from azure.eventhub import EventHubProducerClient, EventData
from azure.eventhub import EventHubProducerClient, EventData



connection_str = 'CONNECTION STRING'
eventhub_name = 'testevents'
client = EventHubProducerClient.from_connection_string(connection_str, eventhub_name=eventhub_name)

event_data_batch = client.create_batch()
event_data_batch.add(EventData('Message 3'))
event_data_batch.add(EventData('Message 2'))

#MAKE A NOTE, MAXIMUM SIZE NEEDS TO BE 1 MB per batch. ABOVE CODE IS ADDING TWO EVENTS
#The above two events are below 20 bytes and hence will work

#Send the messages
with client:
    client.send_batch(event_data_batch)

