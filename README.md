# HeroesAndVillainsLab
Project
Tech Stack
Python, Django/Django REST Framework, MySQL, Postman
User Stories
Total Unweighted Project Points: /47.5
Total Weighted Project Points: / 20
 

 
Main Stories
 
(/2.5 points) As a developer, I want to make good, consistent commits.  

(/2.5 points) As a developer, I want to create an ERD with two tables - Super and SuperType. 
The two tables should show all of the correct properties for both entities as well as the correct relationship between the two tables
 
(/2.5 points) As a developer, I want to create a SuperType model in a “super_types” app. 
Property names must be in snake_case and match the following exactly! 
type – CharField     
 
(/5 points) As a developer, I want to register the SuperType model with the admin site so I can: 
Register a new super user (python manage.py createsuperuser) 
Visit the admin site 
Seed two values (“Hero” and “Villain”) into the “super_type” table 
 
(/2.5 points) As a developer, I want to create a Super model in a “supers” app. 
Property names must be in snake_case and match the following exactly! 
name - CharField 
alter_ego  - CharField 
primary_ability - CharField 
secondary_ability – CharField 
catchphrase – CharField 
super_type – ForeignKey 
 
(/2.5 points) As a developer, I want my API to serve the “supers” app’s content on the following urls paths: 
Paths must match these exactly! 
‘127.0.0.1:8000/api/supers/' - optional params 
‘127.0.0.1:8000/api/supers/<int:pk>/’ 
 
(/5 points) As a developer, I want to create a GET by id endpoint that does the following things: 
Accepts a value from the request’s URL (The id of the super to retrieve). 
Returns a 200 status code. 
Responds with the super in the database that has the id that was sent through the URL. 
 
(/5 points) As a developer, I want to create a POST endpoint that does the following things: 
Accepts a body object from the request in the form of a Super model. 
Adds the new super to the database. 
Returns a 201 status code. 
Responds with the newly created super object. 
 
(/5 points) As a developer, I want to create a PUT endpoint that does the following things: 
Accepts a value from the request’s URL (The id of the super to be updated). 
Accepts a body object from the request in the form of a Super model. 
Finds the super in the Super table and updates that super with the properties that were sent in the request’s body. 
Returns a 200 status code. 
Responds with the newly updated super object. 
 
(/5 points) As a developer, I want to create a DELETE endpoint that does the following things: 
Accepts a value from the request’s URL. 
Deletes the correct super from the database 
Returns a 204 status code (NO CONTENT). 
 
(/10 points) As a developer, I want to create a GET endpoint that responds with a 200 success status code and all of the supers within the supers table. 
This view function should be implemented in a way to accept a “type” parameter 
Example: " http://127.0.0.1:8000/api/supers?type=hero” 
If a type query parameter is sent to the view function with the value of “hero”, the view function response should be a list of all supers that are associated with the type of “Hero” (Shown in End Result Overview video on portal) 
If a type query parameter is sent to the view function with the value of “villain”, the view function response should be a list of all supers that are associated with the type of “Villain” (Shown in End Result Overview video on portal) 
If no type query parameter is sent, return a custom dictionary response with a “heroes” key set equal to a list of supers of type “Hero” and a “villains” key set equal to a list of supers of type “Villain” (Shown in End Result Overview video on portal) 
CODE HINT: custom_response = { “heroes”: [], “villains”: [] } 
In the above code hint we have created a dictionary with two keys, “heroes” and “villains”. After the creation of this dictionary we want to set the “heroes” key equal to all of the heroes from the super table, then set the “villains” key equal to the villains from the super table.
It is this “custom_response” dictionary that we will send in the Response function! (only if no query param was sent in the GET request)

Bonus Stories

(5 points): As a developer, I want to add full CRUD functionality for the “super_type“ table within the “super_types” views.py file.
Checklist

Run through the Setup Setups and get your project ready to begin work.
Review the Resources outlined below - be sure to have relevant documentation and references open while you develop!
Create an ERD diagramming both models for the project and submit to instruction
Complete Django REST API backend by implementing the endpoints

Setup Steps

Make a GitHub Repository (** with Python gitignore **)  
Clone down repository to local computer 
Open folder in VS code and create/activate a local venv 
“pipenv install” 
“pipenv shell” 
Select the correct Python interpreter for the project 
Install all necessary packages 
“pipenv install django” 
“pipenv install djangorestframework” 
Windows - “pipenv install mysqlclient” 
Mac - “pipenv install mysql-connector-python==8.0.26” 
Create an initial Django project  
“django-admin startproject heroes_villains_project .” 
Create a local_settings.py file and import it into your settings.py file to prevent your settings from being pushed to the public repository.  
Cut & Paste DATABASES and SECRET_KEY from settings.py to local_settings.py. Change DATABASES to reflect the appropriate database NAME, ENGINE, USERNAME, PASSWORD, etc. 

Windows: 

    Mac: 

Push project to GitHub repo. 
Create database in MySQL Workbench 
Execute migrations commands 
“python manage.py migrate” 
Create a new app for the supers, and an app for “super_types” 
“python manage.py startapp supers” 
“python manage.py startapp super_types” 
Download the Postman collection (available on your online portal) and import the collection into Postman (File > Import, then upload the file into the window that pops up).  
Postman will create a folder in your list of collections. This folder will contain all of the test requests that you will be building your API to successfully pass. 
 

Resources
PowerPoints
Intermediate Django REST Framework
Relevant Projects 
Products API
Django REST API Tutorial (13 videos)

End Result
Your API will have all features as required by the user stories, and all of the requests provided in the Postman collection will have passed with success codes! 
