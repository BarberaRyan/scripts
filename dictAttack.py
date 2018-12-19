import sys
import hashlib
#Program takes in a string representing the hash of the password, then executes a dictionary attack
#Is currently case sensitive
def dict(a):
	with open('betterdict.txt') as f:
		words = f.read().split()
		
	for word in words:
	
	    #comp = hashlib.md5(word.encode('utf-8')).hexdigest()
		
		if a == word:
			return  "Password found: " + word
	return "The Password was not found"
	
if __name__ == "__main__":
	a = sys.argv[1]
	print(a)
	print(dict(a))


   
	