import glob
import logging
import time
import requests

import paho.mqtt.client as mqtt

# log to a file
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/tmp/mqtt-receive-voice-command.log',
                    filemode='w')

# # log to std output
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(levelname)s %(message)s')

#base_dir = '/sys/bus/w1/devices/'
#device_folder = glob.glob(base_dir + '28*')[0]
#device_file = device_folder + '/w1_slave'

topic_prefix = "pippo@pippo.net"
command_topic = topic_prefix + "/command"
status_topic = topic_prefix + "/status"

URL = "https://free.currencyconverterapi.com/api/v5/convert"


#def read_temperature_raw():
#    f = open(device_file, 'r')
#    lines = f.readlines()
#    f.close()
#    return lines


#def read_temperature():
#    lines = read_temperature_raw()
#    while lines[0].strip()[-3:] != 'YES':
#        time.sleep(0.2)
#        lines = read_temperature_raw()
#    equals_pos = lines[1].find('t=')
#    if equals_pos != -1:
#        temp_string = lines[1][equals_pos + 2:]
#        temp_c = float(temp_string) / 1000.0
#        return temp_c


# This is the Subscriber

def on_connect(client, userdata, flags, rc):
    logging.debug("Connected with result code " + str(rc))
    client.subscribe(command_topic)
    logging.debug("subscribed to " + command_topic)


def on_message(client, userdata, msg):
    text = msg.payload.decode().lower()
    logging.debug("received text: " + text)
    print(f"received text: {text}\n")
    logging.debug("recognized command: ")
    print("recognized command: ")
    if "temperature" in text and "room" in text:
        logging.debug("temperature")
        temp = "273K" # read_temperature() # stubbed here
        logging.debug(temp)
        print ("temperature: {0}\n".format(temp))
        client.publish(status_topic, temp)
        # client.disconnect()
    elif "light" in text and "on" in text:
        logging.debug("light on")
        print ("light on")
        client.publish(status_topic, "on")
    elif "light" in text and "off" in text:
        logging.debug("light off")
        print ("light off")
        client.publish(status_topic, "off")
    else:
        logging.debug("unknown command")
        print("unknown command\n")
        client.publish(status_topic, "unknown command")


client = mqtt.Client()



client.username_pw_set("emqx", "public")
client.connect("broker.emqx.io", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
