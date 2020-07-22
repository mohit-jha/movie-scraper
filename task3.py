from task1 import scrap_top_movie
from pprint import pprint
m=scrap_top_movie()
def group_by_decade(movies):
	year_decade=[]
	for i in movies:
		year=i['year']
		years=""
		for k in range(1,5):
			j=year[k]
			years+=j
		# print(years)
		dec=int(years)%10
		decade=int(years)-dec
		if decade not in year_decade:
			year_decade.append(decade)
			year_decade.sort()
	empty_list={i:[]for i in year_decade}
	for i in movies:
		year=i['year']
		years=""
		for k in range(1,5):
			j=year[k]
			years+=j 
		for x in empty_list:
			last=x+9
			print(last)
			if int(years) >= x and int(years)<=last:
				empty_list[x].append(i)
	return empty_list
pprint(group_by_decade(m))  