import hashlib 
import string
import argparse
from itertools import product
import multiprocessing as mp
import os


def myhash(mot):
	mot = "".join(mot)
	if passwd == hashlib.md5(bytes(mot, "utf8")).hexdigest():
		print("mot :", mot)
		os.kill(os.getppid(), 9)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-l", "--len", type=int, help="len of the password is know")
	parser.add_argument("-m", "--maxlen", default=8, type=int, help="len max of the password to test")
	parser.add_argument("-v", "--verbose", default=0, type=int, choices=[0,1,2])
	parser.add_argument("-p", "--passwd", help="hash to crack")
	args = parser.parse_args()
	
	if args.passwd is None:
		passwd = input("password hash md5 :")
		print("\n",passwd,"\n...", sep="")
	else:
		passwd = args.passwd

	if args.len is not None:
		l = args.len
		args.maxlen = args.len +1
	else:
		l = 1
  
	while l < args.maxlen: # taille max
		with mp.Pool(mp.cpu_count()-1) as p:
			p.imap(myhash,
                product(string.printable.replace(string.whitespace,""), repeat=l),
                chunksize=2000)
			p.close()
			p.join()
		l += 1