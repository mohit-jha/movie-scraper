#this task for finding movie relg... lang
import json
from collections import Counter
file=json.load(open('task4.json','r'))
s=[]
for i in file:
	f=i['language_name']
	for j in f:
		s.append(j)
# print(Counter(s))
my_dict = {x:s.count(x) for x in s}
print((my_dict))

