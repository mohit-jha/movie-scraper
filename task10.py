import json
file=json.load(open('task4.json','r'))
s=[]
director_names=[]
for i in file:
	direc=i['director_name'],i['language_name']
# 	dire=(direc[0])
# 	dict_l=direc[1:]
# 	director_names.append(dire)
# for j in dict_l:
# 	 if j in direc:
	 	
# 	# print(director_names)
# e_dict={i:[dict_l] for i in director_names}
	print(direc)




