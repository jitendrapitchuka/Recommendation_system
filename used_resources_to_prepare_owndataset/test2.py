import csv
from imdbpie import Imdb
import json
imdb=Imdb()

#list=[114709,113497,113228,114885,1013041]

#list=['113497','114709','117060','304141','1457767','4786282','113283']
list=['113610']
list2=[]
for x in list:
    
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
    print(answer)

    
    #print(answer['plot']['summaries'][0].keys())

    if answer['base']['titleType']=="movie" or "tvMovie" and answer['base']['titleType']!="tvEpisode":
        l=answer['base']['image']['url']
        if 'outline' in answer['plot'].keys():
            lu=answer['plot']['outline']['text'] 
        elif 'text' in answer['plot']['summaries'][0].keys():
            lu= answer['plot']['summaries'][0]['text']
            
    #elif answer['base']['parentTitle']['titleType']=="tvSeries":
     #   l=answer['base']['parentTitle']['image']['url']
    
    else:
        lu=""
    print(lu)
    #list1=[l]

    #list2.append(list1)
    #print(list2)





 