import json, os,random,time
import json,requests
from  bs4 import BeautifulSoup
from task1 import scrap_top_movie
from pprint import pprint

from task1 import scrap_top_movie
tittle= scrap_top_movie()
file=json.load(open("task4.json","r"))
count=0

# for i in tittle:
	
function=scrap_top_movie()
def movie_details(function):
	sleeps=random.randint(1,3)
	main_list=[]
	for z in function:


		task_4={}
		urlll=z['link']
		time.sleep(sleeps)
		url=requests.get(urlll).text    	
		soup=BeautifulSoup(url,'html.parser')
		div=soup.find('div',class_='title_wrapper')
		name = div.h1.text.split('(')
		name=(name[0])
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
		task_4['movie_name']=name
		task_4['director_name']=director
		task_4['language_name']=language_data
		task_4['country']=countryy
		task_4['poster_link']=poster
		task_4['genre']=zener_data
		# task_4['movie_name']=name
		main_list.append(task_4)
		a=z["link"]
		a=a.split("/")
		a=a[-2]
		efile=open('mohit/task9/'+a+'.json','w')
		raw=json.dump(task_4,efile,indent=4)
		# efile.write(raw)
		efile.close()
	return(task4)
	# print(task4)
abc=(movie_details(function))



