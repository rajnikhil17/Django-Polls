Open the Application Directory
   	 cd Django-Polls/mysite
    
Run 
python manage.py migrate ----For Migrations(Database)
python manage.py runserver ----Starting Server


localhost:8000/admin------for Admin Page
 
      python manage.py createsuperuser -----> Create another admin
      
      
localhost:8000/polls------for Polls Application

localhost:8000/todos------for todos Application

localhost:8000/music-------for Music Application



Docker Environment

git clone https://github.com/rajnikhil17/Django-Polls.git 

cd Django-Polls/mysite
 
Then Run 

docker-compose up

Now, This Application can be served on Docker Environment as well as on Kubernetes.


