from imdbpie import Imdb
import json
imdb=Imdb()


#print(imdb.get_title('tt0111161'))
list=['tt0114709','tt0113497','tt0113228','tt0114885','tt1013041','tt1980209']





f=open('g.html','w')
html_top="""


<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>


"""
html_template="""







 
<div class="container">
  <h2>Card Image</h2>
  <div class="card" style="width:200px">
    <img class="card-img-top" src="{}" alt="Card image" style="width:100%" class="rounded">
    <div class="card-body">
      <h4 class="card-title">John Doe</h4>
      <p class="card-text">Some example text </p>
    </div>
  </div>
  <br>
  
 




"""
html_str=""

for x in list:
    print(type(x))
    answer=imdb.get_title(x)
   
    if answer['base']['titleType']=="movie":
        l=answer['base']['image']['url']
        html_str+=html_template.format(l)
    elif answer['base']['parentTitle']['titleType']=="tvSeries":
        y=answer['base']['parentTitle']['image']['url']
        html_str+=html_template.format(y)

f.write(html_top+html_str)
f.close()



 