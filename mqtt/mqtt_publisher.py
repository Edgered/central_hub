import paho.mqtt.publish as publish
import argparse


def main():
 

    parser = argparse.ArgumentParser(description='set input file')
    parser.add_argument('path_name', type=str, 
            help='select path name', default='lpu2hub')
    parser.add_argument('payload_name', type=str, 
            help='select the payload', default='hello from LPU')
    parser.add_argument('server_name', type=str, 
            help='select the server_name', default='localhost')
    

    args = parser.parse_args()
    print("argument is ", args)
    
    # MQTT_SERVER = args.server_name
    # MQTT_PATH = args.path_name
    
    # publish (topic, payload=None, hostname=None)
    publish.single(args.path_name, args.payload_name, hostname=args.server_name)
    print("publishing ends")
    
if __name__ == '__main__':
    main()