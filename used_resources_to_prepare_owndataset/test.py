import csv
from imdbpie import Imdb
import json
imdb=Imdb()

filename=open('result.csv')

file=csv.DictReader(filename)

li=[]
for col in file:
    li.append(col['imdbId'])



list2=[]
for x in li:
    temp=x
    x=int(x)
    
    count = 0
    ans=x
    while ans!= 0:
        ans //= 10
        count += 1
    
    if count==6:
        x=str(x)
        
        x="tt0"+x
        
    elif count==7:
        x=str(x)
        x="tt"+x
    elif count==5:
        x=str(x)
        x="tt00"+x

    answer=imdb.get_title(x)
    #print(answer.keys(),temp)
    if answer['base']['titleType']=="movie":
        l=answer['base']['image']['url']
        lu=answer['plot']['outline']['text']
        
        
    elif answer['base']['parentTitle']['titleType']=="tvSeries":
        l=answer['base']['parentTitle']['image']['url']
        lu=""
      
    print(lu,temp)
    #list1=[temp,l,lu]
    
   # list2.append(list1)
    #print(list2)

"""fields=['id','image_url','description']       
li=[x,'l',lu]

with open('result1.csv','w') as file:
    write=csv.writer(file)
    write.writerow(fields)
    write.writerows(li)"""