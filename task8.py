import json, os

from task1 import scrap_top_movie
tittle= scrap_top_movie()
# print(link)
# 	# print(links)
# def title_find(x):
# 	for i in x:
# 		tittle=i['link']
# 		print("__________________________________________")
# 	return(tittle)
# print(title_find(tittle))

file=json.load(open("task4.json","r"))
count=0

for i in tittle:
	a=i["link"]
	a=a.split("/")
	a=a[-2]
	data=open(a+".json","w")
	files=file[count]
	filed=json.dump(files,data,indent=4)
	count+=1



