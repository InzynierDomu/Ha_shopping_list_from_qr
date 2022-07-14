import cv2
import time
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

buzzer_pin = 4

ha_host = '192.168.1.139'
port = 1883
timeout = 60
topic = "test/shopping"
Qos = 0
ha_user = "ha_user"
ha_pass = "ha_pass"

def on_connect(client, userdata, flags, rc):
  print("error = "+str(rc))
  
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

client = mqtt.Client()
client.on_connect = on_connect
client.username_pw_set(ha_user, ha_pass)

client.connect(ha_host, port, timeout)  
  
# set up camera object                                                                                     
cap = cv2.VideoCapture(0)                                                                                  
 
# QR code detection object                                                                                 
detector = cv2.QRCodeDetector()                                                                            

while True:                                                                                                
    # get the image                                                                                        
    _, img = cap.read()                                                                                    
    # get bounding box coords and data                                                                     
    data, bbox, _ = detector.detectAndDecode(img)                                                          
  
    # if there is a bounding box, draw one, along with the data                                            
    if(bbox is not None):                                                                                  
#        for i in range(len(bbox)):                                                                         
#            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255,                
#                     0, 255), thickness=2)                                                                 
#        cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,    
#                    0.5, (0, 255, 0), 2)                                                                   
        if data:                                                                                           
            print("data found: ", data)
            client.publish(topic, data, 0)
            buzz = GPIO.PWM(buzzer_pin, 4186)
            buzz.start(50)
            time.sleep(0.2)
            buzz.start(0)
            time.sleep(4)	
			
# free camera object and exit  
client.disconnect()                                                         
cap.release()                                                                                              
cv2.destroyAllWindows()