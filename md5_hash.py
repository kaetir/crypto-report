import hashlib 
from sys import argv

# print the md5 of the arguments 
[print(hashlib.md5(bytes(a, "utf8")).hexdigest()) for a in argv[1:]]
 