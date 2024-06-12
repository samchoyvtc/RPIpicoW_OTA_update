import time
import ubinascii
import network
import ugit
import sys
# Add the 'libs' directory to the module search path
sys.path.append('/Library')
from umqttsimple import MQTTClient



ssid = 'BN1000ST1'
password = '!vtcvtc!'
mqtt_server = 'broker.emqx.io'
mqtt_user = ''
mqtt_pass = ''

#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify('mqttx_ee5003e0')
topic_sub = b'Sam_notification'
topic_pub = b'Sam_hello'

last_message = 0
message_interval = 10
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())


def sub_cb(topic, msg):
  print((topic, msg))
  print("sub_cb")
  if topic == b'Sam_notification' and msg == b'test':
    print('ESP received hello message')
    ugit.pull_all()
    

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server, user=mqtt_user, password=mqtt_pass)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()


try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
  except OSError as e:
    restart_and_reconnect()



    


