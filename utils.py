import math, os, time

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def file_size_human_readable(filename):
    if os.path.isfile(filename):
        return convert_size(os.path.getsize(filename))
    else:
        return "Not a file"
    
    
class timeDiff():
    def __init__(self):
        self.t0 = time.perf_counter_ns()
        
    def get_diff(self):
        return time.perf_counter_ns() - self.t0
    
    def get_diff_in_s(self):
        return round(self.get_diff()/10**9, 3)