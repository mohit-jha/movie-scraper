# task5.py
import json,requests
from  bs4 import BeautifulSoup
from task1 import scrap_top_movie
function=scrap_top_movie()
urlll=[]
task4=[]
for ur in function:
	urll=ur['link']
	urlll.append(urll)

for i in range(20):
	task_4={}
	link_url=(urlll[i])
	url=requests.get(link_url).text    	
	soup=BeautifulSoup(url,'html.parser')
	div=soup.find('div',class_='title_wrapper')
	name = div.h1.text.split('(')
	names=(name[0])
	# print(names)
	director=soup.find('div',class_='credit_summary_item').a.text
	# print(director)
	try:
		language_tag=soup.find('div',attrs={'class':'article','id':'titleDetails'})
		country=language_tag.findAll('div',class_='txt-block')
		language_data=[]
		for i in country:
			x=i.find('h4').text
			# print(x)
			if x==('Country:'):
				countryy=i.find('a').text
				countryy=(countryy)
			if x==('Language:'):
				language=i.findAll('a')
				for x in language:
					p=(x).text
					language_data.append(p)
			# print(language_data)
			
	except AttributeError :
		pass
			
	# print(language_data)
	poster=soup.find('div',class_='poster')
	poster=poster.find("img")['src']
	# print(poster)
	zener_data=[]
	zener=soup.find('div',class_='subtext')
	zener=zener.findAll('a')
	for y in zener:
		dat=y.text
		zener_data.append(dat)
	zener_data.pop()
	# print(zener_data)
	# print("________________________________________________________")

	##########################################################333
	task_4['movie_name']=names.strip()
	task_4['director_name']=director
	task_4['language_name']=language_data
	task_4['country']=countryy
	task_4['poster_link']=poster
	task_4['genre']=zener_data
	# task_4['movie_name']=name
	task4.append(task_4)
with open('task5''.json','w') as data:
	json.dump(task4,data)
print(task4)
