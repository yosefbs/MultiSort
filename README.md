# MultiSort
## setup
### data base
pull mariadb docke image:

`docker pull mariadb:10.5.9`

start mariadb as docker (user and password are "root"):

`docker run --name=database -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mariadb:10.5.9`

### python venv
create new python venv (for example):

`python -m venv c:\myVenv`

install requirements (`pip install -r requirements.txt`)

### data base init
run dbInitializer.py


##run apps
 run:
  
 sortA.py
 
 
 sortB.py
 
 
 sortCCaller.py
 
 
 resultsWriter.py 
 