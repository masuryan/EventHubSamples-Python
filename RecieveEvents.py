import logging
from azure.eventhub import EventHubConsumerClient

connection_str = 'CONNECTIONSTRING'
consumer_group = '$Default'
eventhub_name = 'testevents'
client = EventHubConsumerClient.from_connection_string(connection_str, consumer_group, eventhub_name=eventhub_name)



def on_event(partition_context, event):
    print("Received event from partition {}".format(event.body_as_str(encoding='UTF-8')))
    partition_context.update_checkpoint(event)

with client:
    client.receive(
        on_event=on_event,
        starting_position="-1",  # "-1" is from the beginning of the partition.
    )
    # receive events from specified partition:
    # client.receive(on_event=on_event, partition_id='0')
