# input.py
# Steven Tsang May 2022
# Description: A python script that will print out a phrase or an array of letters using pynput.

from pynput.keyboard import Key, Controller
import time, random

timesToSpam = 8 # time to repeat the phrase
waitTime = 5 # wait time before starting

print("Starting in", waitTime, "seconds...")

for i in range(waitTime):
    print(waitTime-i)
    time.sleep(1)

keyboard = Controller()

# test, only used in testing
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z']

# enter a phrase here to print out
myOriginalPhrase = "Test Phrase."
myPhrase = myOriginalPhrase

for i in range (timesToSpam):
	for letter in myPhrase:
		keyboard.press(letter)
		keyboard.release(letter)
		
		# alphabet testing
		#keyboard.press(Key.enter)
		#keyboard.release(Key.enter)
		#time.sleep(1/(len(alphabet))) # set this to put a delay
		
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	
	# tries to concatenate a random number with the string to cheat easy anti-spammer.
	myPhrase =  myOriginalPhrase + " " + str(random.randrange(1,100))
