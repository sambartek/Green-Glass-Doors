import time
alphabet = [chr(i) * 2 for i in range(ord('a'), ord('z') + 1)]
space = "*****"

def start():	
	print "Hello and welcome to the Green Glass Doors!"
	time.sleep(2)
	choice = raw_input("Would you like to play Green Glass Doors? y/n >> ")
	if choice == "y":
		print space
		time.sleep(2)
		print "Only certain things are allowed in the Green Glass Doors."
		print space
		time.sleep(2)
		print "For example, coffee is allowed, but not tea."
		print space
		time.sleep(2)
		print "Root beer is allowed, but not Pepsi."
		print space
		time.sleep(2)
		print "You cannot use any of the examples listed above."
		print space
		time.sleep(2)
		begin()	
	elif choice == "n":
		print space
		print "Alright maybe next time."
	else:
		print space
		print "Sorry I didn't understand that."
		
def begin():
	item = raw_input("What would you like to bring through the Green Glass Doors? >> ")
	if any(x in item for x in alphabet):
		print space
		print "Yes that is allowed!"
		retry()
	else:
		print space
		print "No sorry that is not allowed."
		time.sleep(1)
		print space
		retry()
		
def retry():
	again = raw_input("Would you like to try again? y/n >> ")
	if again == "y":
		begin()
	elif again == "n":
		print space
		print "Thank you for playing!"
	else:
		print space
		print "Sorry I didn't understand that."
start()
