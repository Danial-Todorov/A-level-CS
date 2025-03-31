import json 
 
#open the file
with open('/home/user/A-level-CS/Random Lesson Stuff/Exchanging data/JSON_List.txt') as f:
  data = json.load(f)
 
#reading file
print(data)

for person in data["employees"]:
    if person["salary"] >= 7000:
        print(person["name"], "Department is:", person["Dept"])



