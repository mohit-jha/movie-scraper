from task1 import scrap_top_movie
from pprint import pprint
year_l= scrap_top_movie()
def group_by_year(movies):
	years=[]
	
	for i in movies:
		year=i['year']
		if year not in  years:
			years.append(year)
	movie_dict={i:[]for i in years}
	for i in movies:
		year=i['year']
		for x in movie_dict:
			if str(x)==str(year):
				movie_dict[x].append(i)
	return movie_dict
pprint(group_by_year(year_l))






























