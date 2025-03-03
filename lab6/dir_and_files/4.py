import os
import string

with open("c:/Users/kadae/Desktop/python/all_labs_pp2/lab6/examples/example.txt") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
f.close()