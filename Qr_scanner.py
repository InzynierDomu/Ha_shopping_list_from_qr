import paho.mqtt.client as mqtt
import mysql.connector

ha_host = '192.168.1.139'
port = 1883
timeout = 60
topic = "test/shopping"
Qos = 0
ha_user = "ha_user"
ha_pass = "ha_pass"

mydb = mysql.connector.connect(
  host="localhost",
  user="scaner",
  password="scan",
  database="qr"
)

def on_connect(client, userdata, flags, rc):
  print("error = "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.username_pw_set(ha_user, ha_pass)

client.connect(ha_host, port, timeout)    

mycursor = mydb.cursor()                                                                          

while True:   
    code = input('code:')
    sql = "SELECT name FROM codes WHERE qr LIKE " + code
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    print(myresult)
    client.publish(topic, myresult[0], 0)                

client.disconnect()                                                         