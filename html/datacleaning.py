# importing csv module
import csv
  
# csv file name
filename = "../data/policekillings.csv"
  
# initializing the titles and rows list
fields = []
rows = []
dataset2 = [
				{"name": "Asian", "count": 132, "x": 0, "y":0, 'con': []},
				{"name": "Pacific Islander", "count": 49, "x": 0, "y":0, 'con': []},
				{"name": "Native American", "count": 124, "x": 0, "y":0, 'con': []},
				{"name": "Black", "count": 2240, 'x': 0, 'y':0, 'con': []},
				{"name": "Hispanic", "count": 1536, 'x': 0, 'y':0, 'con': []},
				{"name": "White", "count": 3899, 'x': 0, 'y':0, 'con': []},
				{"name": "Unknown Race", "count": 1058, 'x': 0, 'y':0, 'con': []}
			]  

# reading csv file
# import pandas as pd
# df = pd.read_csv(filename, encoding="utf8")
# # saved_column = df.column_name #you can also use df['column_name']
# print(len(df))
# df = pd.DataFrame(df)
# for i in df.iterrows():
# #         print(temp)
# #         var enc = data[i]["Encounter Type (DRAFT)"]
# #         var cause = data[i]["Cause of death"]
#     print(i["Victim's race"])

from csv import DictReader
# iterate over each line as a ordered dictionary and print only few column by column name
with open(filename, 'r', encoding="utf8") as read_obj:
    csv_dict_reader = DictReader(read_obj)
    for row in csv_dict_reader:
        temp = row["Victim's race"]
        enc = row["Encounter Type (DRAFT)"]
        cause = row["Cause of death"]
        if(temp.lower().find("unknown race") != -1 or temp == ""): temp = "Unknown Race"
        elif (temp.lower().find("hispanic") != -1): temp = "Hispanic"
        elif (temp.lower().find("white") != -1): temp = "White"

        if (enc.lower().find("domestic") != -1): enc = "Domestic Violence"
        elif (enc.lower().find("health") != -1 or enc.lower().find("mental")!=-1): enc = "Health Crisis/Mental Health"
        elif (enc== "" or enc== "#VALUE!" or enc.lower().find("no crime")!= -1 or enc.lower().find("none") != -1 or enc.lower().find("unknown") != -1 or enc.lower().find("unavailable") != -1):
            enc = "None/Unknown"
        elif (enc.lower().find("other") != -1 or enc.lower().find("substance abuse") != -1 or enc.lower().find("suspicious person") != -1 or enc.lower().find("profiling") != -1):
            enc = "Other"
        elif (enc.lower().find("violent") != -1):
            enc = "Part 1 Violent Crime"
        elif (enc.lower().find("person with") != -1 or enc.lower().find("weapon") != -1 or enc.lower().find("stabbing") != -1):
            enc = "Weapon"
        elif (enc.lower().find("traffic") != -1):
            enc = "Traffic"
        elif (enc.lower().find("property") != -1):
            enc = "Property"
        elif (enc.lower().find("public order") != -1):
            enc = "Public Order"

        if(cause.lower().find("asphyxiated") != -1):
            cause = "Asphyxiated"
        if (cause.lower().find("pepper spray") != -1):
            cause = "Pepper Spray"
        if (cause.lower().find("physical restraint") != -1):
            cause = "Physical Restraint"
        if (cause.lower().find("bean") != -1):
            cause = "Bean Bag Gun"
        if (cause.lower().find("beaten") != -1 or cause.lower().find("baton") != -1):
            cause = "Beaten"
        if (cause.lower().find("gunshot") != -1):
            cause = "Gunshot"
        if (cause.lower().find("dog") != -1):
            cause = "Police Dog"
        if (cause.lower().find("taser") != -1):
            cause = "Taser"
        if (cause.lower().find("vehicle") != -1):
            cause = "Vehicle"
        if (cause.lower().find("stab") != -1 or cause.lower().find("instrument") != -1 or cause.lower().find("bomb") != -1 or cause.lower().find("chemical") != -1 or cause.lower().find("less lethal") != -1): 
            cause = "Other"
        for i in dataset2:
            # print(i)
            if (i['name'] == temp): 
                check_enc = False
                check_cause = False
                for j in i['con']: 
                    # console.log("0")
                    if (j['name'] == cause): 
                        check_cause = True
                        j['count'] += 1
                    
                    elif (j['name'] == enc):
                        check_enc = True
                        j['count'] += 1
                
                
                if(check_enc == False): 
                    i['con'].append({"name": enc, "count": 1})
                
                else:
                    check_enc = True

                if(check_cause == False):
                    i['con'].append({"name": cause, "count": 1})
            
                else:
                    check_cause = True
            
    

# for i in dataset2:
#     print(i)
# with open(filename, encoding="utf8") as csvfile:
#     # creating a csv reader object
#     csvreader = csv.reader(csvfile)
      
#     # extracting field names through first row
#     fields = next(csvreader)
#     print(csvreader)
# #     # extracting each data row one by one
#     for row in csvreader:
#         # print(row)
#         temp = row["Victim's race"]
#         print(temp)
#         var enc = data[i]["Encounter Type (DRAFT)"]
#         var cause = data[i]["Cause of death"]
#         // if (enc.toLowerCase().includes("domestic") === true) {
#         // 	enc = "Domestic Violence"
#         // }
#         if(str.toLowerCase() === "unknown race" || str === "") {str = "Unknown Race";}
#         else if (str.toLowerCase().includes("hispanic")){str = "Hispanic"}
#         else if (str.toLowerCase().includes("hispanic")){str = "Hispanic"}
#         else if (str.toLowerCase() === "white"){str = "White"}
# // try
#         if (enc.toLowerCase().includes("domestic")) {enc = "Domestic Violence"}
#         else if (enc.toLowerCase().includes("health")|| enc.toLowerCase().includes("mental")){enc = "Health Crisis/Mental Health"}
#         else if (enc==="" || enc==="#VALUE!" || enc.toLowerCase().includes("no crime")|| enc.toLowerCase().includes("none")|| enc.toLowerCase().includes("unknown")|| enc.toLowerCase().includes("unavailable")){
#             enc = "None/Unknown"
#         }
#         else if (enc.toLowerCase().includes("other") || enc.toLowerCase().includes("substance abuse") || enc.toLowerCase().includes("suspicious person") || enc.toLowerCase().includes("profiling")){
#             enc = "Other"
#         }
#         else if (enc.toLowerCase().includes("violent")){
#             enc = "Part 1 Violent Crime"
#         }
#         else if (enc.toLowerCase().includes("person with")|| enc.toLowerCase().includes("weapon") || enc.toLowerCase().includes("stabbing")){
#             enc = "Weapon"
#         }
#         else if (enc.toLowerCase().includes("traffic")){
#             enc = "Traffic"
#         }
#         else if (enc.toLowerCase().includes("property")){
#             enc = "Property"
#         }
#         else if (enc.toLowerCase().includes("public order")){
#             enc = "Public Order"
#         }
#         // try
#         if(cause.toLowerCase().includes("asphyxiated")) {
#             cause = "Asphyxiated"
#         }
#         if (cause.toLowerCase().includes("pepper spray")){
#             cause = "Pepper Spray"
#         }
#         if (cause.toLowerCase().includes("physical restraint")){
#             cause = "Physical Restraint"
#         }
#         if (cause.toLowerCase().includes("bean")){
#             cause = "Bean Bag Gun"
#         }
#         if (cause.toLowerCase().includes("beaten") || cause.toLowerCase().includes("baton")){
#             cause = "Beaten"
#         }
#         if (cause.toLowerCase().includes("gunshot")){
#             cause = "Gunshot"
#         }
#         if (cause.toLowerCase().includes("dog")){
#             cause = "Police Dog"
#         }
#         if (cause.toLowerCase().includes("taser")){
#             cause = "Taser"
#         }
#         if (cause.toLowerCase().includes("vehicle")){
#             cause = "Vehicle"
#         }
        
#         if (cause.toLowerCase().includes("stab") ||cause.toLowerCase().includes("instrument") || cause.toLowerCase().includes("bomb") || cause.toLowerCase().includes("chemical") || cause.toLowerCase().includes("less lethal")){ 
#             cause = "Other"
#         }
  
#     # get total number of rows
#     print("Total no. of rows: %d"%(csvreader.line_num))
  
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(dataset2))
with open("sample.json", "w") as outfile:
    outfile.write(json.dumps(dataset2))