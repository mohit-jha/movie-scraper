import json,requests,time
# from  bs4 import BeautifulSoup
# from task4 import task4s
# from task1 import scrap_top_movie
from pprint import pprint
# fntn=(task4s(function))
# pprint(fntn)
file=json.load(open('task4.json','r'))
file2=json.load(open('task12.json','r'))
cast=[]
count=0
for x in file:
	cast.append(x)
	cast.append(file2[count])
	cast.append("_____________________________")
	count+=1
pprint(cast)
print("________________________________________")
	
	