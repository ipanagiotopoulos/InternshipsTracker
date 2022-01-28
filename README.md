# InternshipsTracker
You should have **Docker** installed in your local machine and **docker-compose** .

Steps:
 1.cd InternshipsTracker && cp example.env .env
 
 
 2.docker-compose up --build -d
 
 
 3.http://localhost:8001/ will redirect you to the intial page of internships internshipsystem_web service



 4.docker exec -it **CAUTION(internship_web CONTAINER_ID)  /bin/bash


 5.Since you enter  the container then you should run **python3 manage.py create superuser**
  
 
 6.Sometimes you might have to run **python3 manage.py makemigrations && python3 manage.py migrate ** but all is managed by the reload command in the gunicorn sever.


 7.You are ready to go with http://localhost:8001/admin, and create all the users you need.

 
