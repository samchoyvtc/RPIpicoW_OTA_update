import time
import ubinascii
import network
import ugit
import sys
# Add the 'libs' directory to the module search path
sys.path.append('/Library')
from umqttsimple import MQTTClient


#MQTT Info
mqtt_server = 'broker.emqx.io'
mqtt_user = ''
mqtt_pass = ''
client_id = ubinascii.hexlify('mqttx_ee5003e0')
topic_sub = b'OTA_notification'
topic_pub = b'OTA_pub'


def sub_cb(topic, msg):
  print((topic, msg))
  print("sub_cb")
  if topic == b'OTA_notification' and msg == b'OTA_UPDATE':
    print('MESSAGE Received')
    ugit.pull_all()
    

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server, user=mqtt_user, password=mqtt_pass)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

ugit.wificonnect()
try:
  client = connect_and_subscribe()
except OSError as e:
  machine.reset()

while True:
  try:
    client.check_msg()
    client.publish(topic_pub, "OTA Alive")
  except OSError as e:
    restart_and_reconnect()
  time.sleep(5)
    



    




