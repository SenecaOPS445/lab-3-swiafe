#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: Samuel Wiafe swiafe

import subprocess

def free_space():
    
    process = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", 
                               shell=True, 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE)
    
    output, error = process.communicate()
    
    
    if process.returncode == 0:
        return output.decode('utf-8').strip()
    else:
        return "Error: " + error.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
