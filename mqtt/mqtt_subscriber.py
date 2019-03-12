import paho.mqtt.client as mqtt
import argparse
 
MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # more callbacks, etc

def main():
    parser = argparse.ArgumentParser(description='set input file')
    parser.add_argument('path_name', type=str, 
            help='select path name', default='lpu2hub')
    parser.add_argument('server_name', type=str, 
            help='select the server_name', default='localhost') 
    parser.add_argument('timeout', type=int, 
            help='select the timeout', default=60) 
    client = mqtt.Client()
    args = parser.parse_args()

    MQTT_SERVER = args.server_name
    MQTT_PATH = args.path_name

    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect(MQTT_SERVER, 1883, int(args.timeout))
    
    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()

if __name__ == '__main__':
    main()

