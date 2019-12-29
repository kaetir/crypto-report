import hashlib 
import string
import argparse
from itertools import product
import multiprocessing as mp
import os

# function for generating the hash from an char array
def hash_func(word: list):
	"""
	@summary join and hash an array of characters and test the hash with the searched hash
	@return print the password and kill the program
	"""
	word = "".join(word)
	if passwd == hashlib.md5(bytes(word, "utf8")).hexdigest():
		print("word :", word)
		# a bad way to terminate but a one that work 
		# if you have any idea to improve make a pull request
		os.kill(os.getppid(), 9)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-l", "--len", type=int, help="len of the password is know")
	parser.add_argument("-m", "--maxlen", default=8, type=int, help="len max of the password to test")
	parser.add_argument("-v", "--verbose", default=0, type=int, choices=[0,1,2])
	parser.add_argument("-p", "--passwd", help="hash to crack")
	args = parser.parse_args()
	
	# checking if the password is passed as parameter
	if args.passwd is None:
		passwd = input("password hash md5 :")
		print("\n",passwd,"\n...", sep="")
	else:
		passwd = args.passwd

	lenght = 1
	# checking if the lenght is passed as parameter	
	if args.len is not None:
		lenght = args.len
		args.maxlen = args.len +1
	
	
	while lenght < args.maxlen: # max lenght
		# using all cpu core -1 for not freezing the system 
		# remove the -1 for better perfomance for the brute force but less performance for other programs
		with mp.Pool(mp.cpu_count()-1) as p:
			# You can adjust the chunksize it work quite nice on my computer with 2000 but if you increase it
			# too much the ram consumption will be important
			p.imap(hash_func,
                product(string.printable.replace(string.whitespace,""), repeat=lenght),
                chunksize=2000)
			p.close()
			p.join()
		lenght += 1

	# max lenght reached
	print("password not found")