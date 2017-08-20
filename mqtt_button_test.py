#!/usr/bin/env python
import cayenne.client

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "ace55b60-8511-11e7-9727-55550d1a07e7"
MQTT_PASSWORD  = "373de1ee07e33df0ba1f1637c2ab39e2a386a229"
MQTT_CLIENT_ID = "baca0200-8523-11e7-a491-d751ec027e48"


# The callback for when a message is received from Cayenne.
def on_message(message):
    import finger_once_noexit.py
    # print("message received: " + str(message))
    # If there is an error processing the message return an error string, otherwise return nothing.


client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)
client.loop_forever()

