#Version 0.01

import sys
import math
import hashlib
import timeit
lettersLower = 'abcdefghijklmnopqrstuvwxyz'
lettersUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = "0123456789"
allChars = lettersLower + lettersUpper + numbers

#An extremly unsopisticated brute force cracker
#Still needs to account for hashing, which will slow down these estimates further

#Current Time to crack 3 digit password (Worst Case) 0.8209
#Current Time to crack 4 digit password (Worst Case) 57.9297 
#Current Time to crack 5 digit password (Worst Case) estimated 4089 or 1 hour 8 min
#Current Time to crack 6 digit password (Worst Case) Hahahahaha, no this will need either a better algorithm or paralleization (Probably both)



#This program acts as if each digit were a 62-bit number, and counts
#based on the value of n 
def brute(a, b):
	i = 0
	guess = ''

	while(62 ** b > i):
		tmp = i
		for y in range(0,b):
			guess+= allChars[tmp%62]
			tmp = math.floor(tmp/62) 
		if guess == a:
			return "Password is: " + guess
		else:
			i+=1
			guess = ''
	return "Password not found"
	
#Using this program from command line is as follows:
#python bruteForce.py a b
#Where a is the password to be guessed
#And b is the number of characters in the password
	
if __name__ == "__main__":
	a = sys.argv[1]
	b = int(sys.argv[2])
	print(a)
	start = timeit.default_timer()
	print(brute(a, b))
	stop = timeit.default_timer()

	print('Time: ', stop - start)  