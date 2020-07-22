# task1
import requests,json
from pprint import pprint
from bs4 import BeautifulSoup
def	scrap_top_movie():
	url='https://www.imdb.com/india/top-rated-indian-movies/'
	urll="https://www.imdb.com/"
	page=requests.get(url)
	soup=BeautifulSoup(page.text,'html.parser')
	raw_html=soup.find('tbody',{'class':'lister-list'}).findAll('tr')
	movie_list=[]
	rank=[]
	for html in raw_html:
		dict_1={}
		title=html.find('td',{'class':'titleColumn'}).find('a').get_text()
		rating=html.find('td',{'class':'ratingColumn imdbRating'}).find('strong').get_text()
		rating=float(rating)
		year=html.find('span',{'class':'secondaryInfo'}).get_text()
		link=html.find('td',{'class':'titleColumn'}).a['href']
		position=html.find('td',{'class':'titleColumn'}).get_text().strip()
		r=''
		# print(position)
		for o in position:
			if '.' not in o:
				r=r+o
			else:
				break
		# rank.append(r)
		dict_1['position']=(r)
		dict_1['name']=title
		dict_1['rating']=rating
		dict_1['year']=year
		dict_1['link']=urll+link
		movie_list.append(dict_1)
	with open('taskk1.json','w') as data:
		json.dump(movie_list,data)
	return (movie_list)
# pprint(scrap_top_movie())
# 
# def group_by_year(movies):
# m=scrap_top_movie()
	