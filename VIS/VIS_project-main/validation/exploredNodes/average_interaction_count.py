import json

# Opening JSON file

i = 1
count_tutorial = 0
count_task_1 = 0
count_task_2 = 0
count_task_3 = 0
count_task_4 = 0
start_counting = 0
end_tutorial = 0
end_task_1 = 0
end_task_2 = 0
end_task_3 = 0
end_task_4 = 0

max_tutorial = 0
max_task_1 = 0
max_task_2 = 0
max_task_3 = 0
max_task_4 = 0

min_tutorial = 100
min_task_1 = 100
min_task_2 = 100
min_task_3 = 100
min_task_4 = 100

std_tutorial = 0

tmp_tutorial = 0
tmp_task_1 = 0
tmp_task_2 = 0
tmp_task_3 = 0
tmp_task_4 = 0

help_std_tutorial = 0
help_std_task_1 = 0
help_std_task_2 = 0
help_std_task_3 = 0
help_std_task_4 = 0

prev = ''

warning_std = 0


while i <= 49:

    f = open('summary_falcon_7M_' + str(i) + ".json")
    data = json.load(f)

    for el in data["0"]:
        
        if prev == "":
            count_tutorial += 1
            tmp_tutorial += 1
        
        if prev in el:
            count_tutorial += 1
            tmp_tutorial += 1
            
        if prev not in el:
            end_tutorial += 1
            tmp_tutorial = 0
            warning_std = 0
            
        if prev not in el and prev != "":
            warning_std = 1
        
        if "departure" in el:
            prev = "departure"
           
        if "distance" in el:
            prev = "distance"
            
        if "airtime" in el:
            prev = "airtime"
                  
        if "arrival" in el:
            prev = "arrival"
        
        if "delay" in el:
            prev = "delay"
        
        if "count" in el:
            prev = "count"
            
                 
        if tmp_tutorial < min_tutorial: 
            min_tutorial = tmp_tutorial
                
        if tmp_tutorial > max_tutorial:
            max_tutorial = tmp_tutorial
                
            
        if warning_std == 1:
            help_std_tutorial = pow((tmp_tutorial - 3.95), 2) + help_std_tutorial
            
 
    help_std = 0
    prev = ""
    warning_std = 0
    
    for el in data["1"]:

        if prev == "":
            count_task_1 += 1
            tmp_task_1 += 1
        
        if prev in el:
            count_task_1 += 1
            tmp_task_1 += 1
            
        if prev not in el:
            end_task_1 += 1
            tmp_task_1 = 0
            warning_std = 0
            
        if prev not in el and prev != "":
            warning_std = 1
        
        if "departure" in el:
            prev = "departure"
           
        if "distance" in el:
            prev = "distance"
            
        if "airtime" in el:
            prev = "airtime"
                  
        if "arrival" in el:
            prev = "arrival"
        
        if "delay" in el:
            prev = "delay"
        
        if "count" in el:
            prev = "count"
            
                 
        if tmp_task_1 < min_task_1: 
            min_task_1 = tmp_task_1
                
        if tmp_task_1 > max_task_1:
            max_task_1 = tmp_task_1
                
        if(warning_std == 1):    
            help_std_task_1 = pow((tmp_task_1 - 3.92), 2) + help_std_task_1
            
 
    help_std = 0
    prev = ""
    warning_std = 0    
 
    

    for el in data["2"]:
        
        if prev == "":
            count_task_2 += 1
            tmp_task_2 += 1
        
        if prev in el:
            count_task_2 += 1
            tmp_task_2 += 1
            
        if prev not in el:
            end_task_2 += 1
            tmp_task_2 = 0
            warning_std = 0
            
        if prev not in el and prev != "":
            warning_std = 1
        
        if "departure" in el:
            prev = "departure"
           
        if "distance" in el:
            prev = "distance"
            
        if "airtime" in el:
            prev = "airtime"
                  
        if "arrival" in el:
            prev = "arrival"
        
        if "delay" in el:
            prev = "delay"
        
        if "count" in el:
            prev = "count"
            
                 
        if tmp_task_2 < min_task_2: 
            min_task_2 = tmp_task_2
                
        if tmp_task_2 > max_task_2:
            max_task_2 = tmp_task_2
    
        if(warning_std == 1):    
            help_std_task_2 = pow((tmp_task_2 - 3.91), 2) + help_std_task_2
            
 
    help_std = 0
    prev = ""
    warning_std = 0   
    
    
    

    for el in data["3"]:
        
        if prev == "":
            count_task_3 += 1
            tmp_task_3 += 1
        
        if prev in el:
            count_task_3 += 1
            tmp_task_3 += 1
            
        if prev not in el:
            end_task_3 += 1
            tmp_task_3 = 0
            warning_std = 0
            
        if prev not in el and prev != "":
            warning_std = 1
        
        if "departure" in el:
            prev = "departure"
           
        if "distance" in el:
            prev = "distance"
            
        if "airtime" in el:
            prev = "airtime"
                  
        if "arrival" in el:
            prev = "arrival"
        
        if "delay" in el:
            prev = "delay"
        
        if "count" in el:
            prev = "count"
            
                 
        if tmp_task_3 < min_task_3: 
            min_task_3 = tmp_task_3
                
        if tmp_task_3 > max_task_3:
            max_task_3 = tmp_task_3
            
                
        if(warning_std == 1):    
            help_std_task_3 = pow((tmp_task_3 - 3.69), 2) + help_std_task_3
            
 
    help_std = 0
    prev = ""
    warning_std = 0  
    
    
    
    

    for el in data["4"]:
        
        if prev == "":
            count_task_4 += 1
            tmp_task_4 += 1
        
        if prev in el:
            count_task_4 += 1
            tmp_task_4 += 1
            
        if prev not in el:
            end_task_4 += 1
            tmp_task_4 = 0
            warning_std = 0
            
        if prev not in el and prev != "":
            warning_std = 1
        
        if "departure" in el:
            prev = "departure"
           
        if "distance" in el:
            prev = "distance"
            
        if "airtime" in el:
            prev = "airtime"
                  
        if "arrival" in el:
            prev = "arrival"
        
        if "delay" in el:
            prev = "delay"
        
        if "count" in el:
            prev = "count"
            
                 
        if tmp_task_4 < min_task_4: 
            min_task_4 = tmp_task_4
                
        if tmp_task_4 > max_task_4:
            max_task_4 = tmp_task_4
                
        if(warning_std == 1):    
            help_std_task_4 = pow((tmp_task_4 - 4.15), 2) + help_std_task_4
            
 
    help_std = 0
    prev = ""
    warning_std = 0  
    

    i += 1


finalCount = "Tutorial: " + str(count_tutorial) + "," + str(end_tutorial) + ", Min: " + str(min_tutorial) + ", Max: " + str (max_tutorial) + "; " + "Task 1: " + str(count_task_1) + "," + str(end_task_1) + ", Min: " + str(min_task_1) + ", Max: " + str(max_task_1) + "; "  + "Task 2: " + str(count_task_2) + "," + str(end_task_2) + ", Min: " + str(min_task_2) + ", Max: " + str(max_task_2) + "; " + "Task 3: " + str(count_task_3) + "," + str(end_task_3) + ", Min: " + str(min_task_3) + ", Max: " + str(max_task_3) + "; " + "Task 4: " + str(count_task_4) + "," + str(end_task_4) + ", Min: " + str(min_task_4) + ", Max: " + str(max_task_4) + "   //////   " + str(help_std_tutorial) + "," + str(help_std_task_1) + "," + str(help_std_task_2) + "," + str(help_std_task_3) + "," + str(help_std_task_4) 

with open('countFinal.json', 'w') as fp:
            json.dump(finalCount, fp,  indent=4)


f.close()