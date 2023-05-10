import json
i = 1
toWrite = ""
f2 = open("scatter_plot_data.txt")

while(i <= 50):

    f1 = open('summary_falcon_7M_' + str(i) + '.json')
    data = json.load(f1)


    for(el in data["0"]):
   
        count = 0
        
   
    
    i += 1
with open("count" + "_falcon_7M" + '_' + '.json', 'w') as fp:
            json.dump(count, fp,  indent=4)
