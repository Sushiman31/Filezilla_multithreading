import os
    
current_dir = os.path.realpath(os.path.dirname(__file__))
len_to_keep = len(current_dir) - 11
local_dir = current_dir[:-11] + "FTPServerLocal"

print(local_dir)