import json
i = 1
toWrite = ""
f2 = open("scatter_plot_data.txt")
while(i <= 50):
    f1 = open('summary_falcon_7M_' + str(i) + '.json')
   
    count = 0
    data = json.load(f1)

    for el in data:
          toWrite = toWrite + " , " + str(el)
   
    
    i += 1
with open("count" + "_falcon_7M" + '_' + '.json', 'w') as fp:
            json.dump(count, fp,  indent=4)
