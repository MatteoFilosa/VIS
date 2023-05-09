
# Python program to read
# json file
  
  
import json
  
# Opening JSON file
f = open('summary_falcon_7M_11.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data['1']:
    print(i[3])
    
  
# Closing file
f.close()