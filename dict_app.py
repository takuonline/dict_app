import json
from difflib import get_close_matches
import json
import os
import subprocess

data=json.load(open('076 data.json'))

def def_of_word():
    data=json.load(open('076 data.json'))
    
    print("Taku's dictionary app")
    wrd= input('\nlnput the word you want to know the meaning of:\n >>')#.lower
    word=wrd.lower()
    
#     if word == "exit()":
#         subprocess.call("exit",shell=True)
        
    if word in data:
        meaning = data[word]
        
    elif word not in data:
        
        other_word = get_close_matches(word,data.keys(),n=1) 
        
        if other_word == []:
            return 'Sorry the word that u typed in can not be found'
        else:         
            yes_no=input('\nDid you mean >{}< instead \n'.format(str(other_word[0])) +'Type Y for yes and N for no\n>>').lower()
            if yes_no == 'y':
                meaning= data[other_word[0]]
            
            elif yes_no == 'n':
                return 'Sorry the word that u typed in can not be found'
        
            else:
                return '\nSorry we did not get that\n'                                                       
    else:                                                   
        return '\nSorry the word that you typed in cannot be found\n'
    
    for item in meaning:
        
        print(item)
    
    
while True:
    
    def_of_word()
    
    
    
