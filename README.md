# HoodWatch

>[PatriciaAnduru](https://github.com/PatriciaAnduru)

  
# Description  
This is a neigbhourhood watch app, a nyumba kumi and government policing in knowing your your neighbour. In order to join a hood you must sign up then login to be a member of a hood. 

##  Live Link  
 Click [View Site](https://hoodiewatch.herokuapp.com/)  to visit the site


## User Story  
  
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/PatriciaAnduru/neighwatch.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd HoodWatch 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations hood
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  

## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 2.2.6](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
    
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  

## Contact Information   
If you have any question or contributions, please email me at [andurupatricia@gmail.com]  

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/PatriciaAnduru/neighwatch/blob/master/LICENSE)  
* Copyright (c) 2020 **Patricia Anduru**
  
  
 
