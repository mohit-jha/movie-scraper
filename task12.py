import json,requests,time
from  bs4 import BeautifulSoup
from task1 import scrap_top_movie
from pprint import pprint
function=scrap_top_movie()
# def task4s(function):
task4=[]
all_movies_id=[]

cast_lis=[]
for x in function:
	linkk=x['link']
	split_l=(linkk).split('/')
	split_list=(split_l[5])
	link='https://www.imdb.com/title/'+split_list+'/fullcredits?ref_=tt_cl_sm#cast'
	cast_li=[]
	request=requests.get(link).text
	soup=BeautifulSoup(request,"html.parser")
	cast=soup.find('table',class_='cast_list')
	castdata=cast.find_all('td',class_=False)
	# print(castdata	)
	for i in castdata:
		c={}

		a=i.find('a')['href']
		a_split=a.split('/')
		a_splitf=(a_split[2])
		name=i.text.strip()
		# print(name)
		c['id']=a_splitf
		c['name']=name
		# c['_____']='_______________________________________'
		cast_li.append(c)
	cast_lis.append(cast_li)	
print(cast_lis)
file=open('task12.json','w')
file_x=json.dump(cast_lis,file,indent=4)