import json
file=json.load(open('task4.json','r'))
director_name=[]
for x in file:
	direc=x['director_name']
	# if direc not in  director_name:
	director_name.append(direc)
# print(director(director_name))
dict_director={x:director_name.count(x) for x in director_name}
print(dict_director)