#convert linux csv to format readable (flare) by d3
import csv
import json
node_list = []
parents_final = {"name": "origin", "children": [], "start": "1991-01-01", "end":"2018"}
current_working = parents_final["children"]



def FindChild(parent):
    for node in node_list:
        if node[3] == parent["name"]:          
            parent["children"].append({"name" : node[1] , "children" : [],"start" : node[4].replace('.','-') , "end" : node[5].replace('.','-'),"url" : node[7]}) 

    
    
    
with open('gldt.csv', 'rb') as csvfile:
    distroreader = csv.reader(csvfile)
    
    for row in distroreader:
    #search all node lines
        if row[0]=='N' or row[0]=='// N' or row[0]=='#N':
            node_list.append(row)
    
    for node in node_list:
        if node[3] == "":
            parents_final["children"].append({"name" : node[1] , "children" : [],"start" : node[4].replace('.','-') , "end" : node[5].replace('.','-')})   

for x in current_working:
    FindChild(x)  
current_working = current_working[0]["children"]
for x in current_working:
    FindChild(x)   
current_working = current_working[0]["children"]
for x in current_working:
    FindChild(x) 

    
json_file = json.dumps(parents_final, sort_keys=False, indent=4, separators=(',', ': '))
print(json_file)
file_test = open('test.json', 'w')
file_test.write(json_file)        
