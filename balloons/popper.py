from gpiozero import Button, OutputDevice
from time import sleep
import os

os.system('clear')

# Replace the pin number [2,3,4] with correct pinout that you are using.
balloons = [OutputDevice(2), OutputDevice(3), OutputDevice(4)]

user_input = raw_input("\033[92m[+] Press 'Y' to begin balloon popping sequence [Y:n] : ")
print "\033[0m"

current = 1
if user_input is "Y" or user_input is "y":
	for balloon in balloons:
		balloon.on()
		print '\033[91m  [*] Balloon %s is armed. \033[0m' % current
		print '\033[93m  [*] Initiating sleep sequence . \033[0m'
		sleep(10)
		balloon.off()
		print '\033[93m  [*] Balloon %s is disarmed. \033[0m \n' % current
		
		current += 1
	print '\033[92m[+] Sequence completed! \033[0m'
else:
	print "\033[91m[+] Bad input: Exiting...\033[0m"


