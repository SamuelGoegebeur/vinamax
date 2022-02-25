import os
import pandas as pd

def find_func(func):
    directory = 'C:\\Users\\SamuelGGB\\go\\src\\vinamax\\'

    for filename in os.listdir(directory):
        if filename.split('.')[-1]=='go':
            with open(directory+filename) as f:
                lines = f.readlines()
                i = 0
                for line in lines:
                    i+=1
                    l = line.split(' ')
                    if func in l:
                        print(filename, 'line = ',i,'of',len(lines))
                    if func+'\n' in l:
                        print(filename, 'line = ',i,'of',len(lines))
                    if '\t'+func in l:
                        print(filename, 'line = ',i,'of',len(lines))
                    if '\t'+func+'\n' in l:
                        print(filename, 'line = ',i,'of',len(lines))
                    if func+'()' in l:
                        print(filename, 'line = ',i,'of',len(lines))  
                    if '\t'+func+'()' in l:
                        print(filename, 'line = ',i,'of',len(lines))                   
find_func('outputinterval')