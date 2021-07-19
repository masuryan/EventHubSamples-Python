# EventHubSamples-Python
 This Code base has sample python code for sending messages to EventHub using azure-eventhub client SDK (AMQP protocol) and also using REST API end points (HTTP 1.1)
 
 ## Code Structure
 sendEventsAsync.py uses azure-eventhub client SDK (AMQP protocol) and creates single connection <br>
 SendEventstoEventsHubAsync uses azure-eventhub client SDK (AMQP protocol) and creates connection for each batch of events<br>
 SendEventHttpRest uses HTTP1.1 REST API calls.<br>
