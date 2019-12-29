import hashlib 
import string 
from itertools import product

def crack(passwd):
	l = 1
	while l < 15: # taille max
		for e in product(string.printable.replace(string.whitespace,""), repeat=l):
			mot = "".join(e)
			if passwd == hashlib.md5(bytes(mot, "utf8")).hexdigest():
				return mot
		l += 1


if __name__ == "__main__":
	passwd = input("password hash md5 :")
	print("passwd :"+ crack(passwd))