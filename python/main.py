#Motor Side
spacebrewServer = "h1.ryanteck.org.uk"
spacebrewPort = 9000


from spacebrew import Spacebrew
import RPi.GPIO as GPIO
#Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) #m1a
GPIO.setup(18, GPIO.OUT) #m1b
GPIO.setup(22, GPIO.OUT) #m2a
GPIO.setup(23, GPIO.OUT) #m2b


brew = Spacebrew("RTK-000-001", description="A Raspberry Pi with a RTK-000-001 on it", server="h1.ryanteck.org.uk")

#Add the subscribers for the motors
brew.addSubscriber("motor1a", "boolean")
brew.addSubscriber("motor1b", "boolean")
brew.addSubscriber("motor2a", "boolean")
brew.addSubscriber("motor2b", "boolean")


#handy string to boolean found from stack overflow
def str2bool(v):
	return v.lower() in ("yes", "true", "t", "1")

#handlers
def motor1aH(value):
	value = str2bool(value)
        GPIO.output(17, value)
	print "motor1a" + str(value)

def motor1bH(value):
	value = str2bool(value)
        GPIO.output(18, value)
	print "motor1b" + str(value) 

def motor2aH(value):
	value = str2bool(value)
        GPIO.output(22, value)
	print "motor2a" + str(value) 

def motor2bH(value):
	value = str2bool(value)
        GPIO.output(23, value)
	print "motor2b" + str(value) 



try:
	brew.start()
	brew.subscribe("motor1a", motor1aH)	
	brew.subscribe("motor1b", motor1bH)	
	brew.subscribe("motor2a", motor2aH)	
	brew.subscribe("motor2b", motor2bH)	
	

finally:
	brew.stop()
