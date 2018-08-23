Open the Application Directory
    cd Django-Polls/mysite
    
Run 
python manage.py migrate ----Migrations
python manage.py runserver ----Starting Server


localhost:8000/admin------for Admin Page
 
      python mamage.py createsuperuser -----> Create another admin
      
      
localhost:8000/polls------for Polls Application

localhost:8000/todos------for todos Application

localhost:8000/music-------for Music Application


Docker Environment

 cd Django-Polls/mysite
 
Then Run 

"docker-compose up"

Now, This Application can be served on Docker Environment as well as on Kubernetes.
