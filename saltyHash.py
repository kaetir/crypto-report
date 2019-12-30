import hashlib, string, random
from sys import argv

def random_string(string_length: int = 10) -> str:
    """
    @summary genere un mot de passe aléatoire avec minuscules majuscules et ponctuation
    @param string_length: int -> nombre de lettres
    @return str: la phrase de sortie
    """
    letters = string.ascii_letters + string.punctuation + string.digits
    return ''.join(random.choice(letters) for i in range(string_length))


# print the salted md5 of the first arguments 
mot = argv[1]
sel = random_string(30)
print("hash : {}\nsel : {}".format(hashlib.md5(bytes(mot+sel, "utf8")).hexdigest(), sel))