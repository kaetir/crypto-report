import math, os, time


def convert_size(size_bytes: int) -> str:
    """
    @summary convert a size from bytes to human readable format
    @param int size in bytes
    @source https://www.science-emergence.com/Articles/Obtenir-et-formatter-la-taille-dun-fichier-en-octet-avec-python/
    @return string of the size human readable
    """
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "{} {}".format(s, size_name[i])

def file_size_human_readable(filename) -> str:
    """
    @summary convert a size from bytes to human readable format
    @param string path to the file to size
    @return string of the size human readable or File not found
    """
    if os.path.isfile(filename):
        return convert_size(os.path.getsize(filename))
    else:
        return "File not found"
    
    
class timeDiff():
    """
    @summary permit to mesure elapsed time
    """
    def __init__(self):
        self.t0 = time.perf_counter_ns()
        
    def get_diff(self):
        """
        @summary return the elapsed time in nano seconds
        """
        return time.perf_counter_ns() - self.t0
    
    def get_diff_in_s(self):
        """
        @summary return the elapsed time in seconds
        """
        return round(self.get_diff()/10**9, 3)