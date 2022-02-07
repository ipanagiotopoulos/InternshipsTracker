# internships_tracker
You should have **Docker** installed in your local machine and **docker-compose** .

Steps:
 
 
 1.cd internships_tracker && cp example.env .env

 2.open the .env file
 
  2.1 set your postgres db creds
     DB_DATABASE_NAME=
     DB_USERNAME=
     DB_PASSWORD=
     DB_HOST=db
     DB_PORT=


  2.2 set your django superuser creds:
   DJANGO_SUPERUSER_PASSWORD=
   DJANGO_SUPERUSER_USERNAME=
   DJANGO_SUPERUSER_EMAIL=


  2.3 set DJANGO_ALLOWED_HOSTS=localhost to run locally


 3.docker-compose up --build -d
 
 
 4.http://localhost:8000/ will redirect you to the intial page of internships internshipsystem_web service

 5.You are ready to go with http://localhost:8001/admin, and create all the users you need.

 6.You can make live changes to the code , and wwsgi server in internships_web container reloads everytime when there is no runtime error.


##steps that might be needed

 1.docker exec -it **CAUTION(internship_web CONTAINER_ID)  /bin/bash


 2.Since you enter  the container then you should run **python3 manage.py create superuser**
  
 
 3.Sometimes you might have to run **python3 manage.py makemigrations && python3 manage.py migrate ** but all is managed by the reload command in the gunicorn sever.





 
