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
            enc = "Other Type"
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
        if (cause.lower().find("stab") != -1 or cause.lower().find("instrument") != -1 or cause.lower().find("bomb") != -1 or cause.lower().find("chemical") != -1 or cause.lower().find("less lethal") != -1 or cause.lower().find("other") != -1): 
            cause = "Other Cause"
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