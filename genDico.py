# coding: utf8
import hashlib, string
import argparse
from itertools import product
from multiprocessing import Pool, cpu_count
from utils import timeDiff, file_size_human_readable

# function for generating the hash from an char array
def hash_func(word: list) -> str:
	"""
	@summary join and hash an array of characters
	@return the concatenation of the word and the hash
	@return_format {word},{hash}
	"""
	word = "".join(word)
	return word +","+ hashlib.md5(bytes(word, "utf8")).hexdigest()


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--filename", default="/tmp/dico.table", help="file to save the dict")
	parser.add_argument("-l", "--len", default=4, type=int, help="len of the password to generate the password list")
	parser.add_argument("-v", "--verbose", default=0, type=int, choices=[0,1,2])
	args = parser.parse_args()
	
	t = timeDiff()
	with open(args.filename, "w") as di:
		# using all cpu core -1 for not freezing the system 
		# remove the -1 for better perfomance for the brute force but less performance for other programs
		with Pool(cpu_count()-1) as p:
			# You can adjust the chunksize it work quite nice on my computer with 2000 but if you increase it
			# too much the ram consumption will be important
			tab = p.imap(hash_func, 
						product(string.ascii_letters + string.punctuation + string.digits, 
			  			repeat=args.len),
						chunksize=2000)
			p.close()
			p.join()
		di.write("\n".join(tab))
	
	if args.verbose > 0:
		print("time to generate the table : {}s".format(t.get_diff_in_s()))
	if args.verbose == 2:
		print("the generated file is {}".format(file_size_human_readable(args.filename)))