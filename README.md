# Mini Social Media APP Created with Django and SQLite
The mini social media app allows users to create profiles, login, logout, submit posts, comment and like posts, and follow other users. This is a mobile responsive site. I used Python, Django and SQLite for the backend system. This was the project requirment from CS50Web Lecture 7, Project 4.

Django Model creation was challenging to understand the many-to-many relationship in SQL. I remember having trouble with the post creation and how it is connected to each user to view, like and comment. I kept running into the issue of not having multiple users able to like or comment. It took me a bit to trouble shoot and understand but I figured it out within a few hours of creation.

## How to install and run the project

### clone this repository with
```
git clone https://github.com/alexjohn7516/mini-social-media.git
```

to pull the repository into your folder.

There is already a virtual environment set up so activate it using

```
source ./venv/bin/activate
```
then download the files using
```
pip -r install requirements.txt
```
make sure you are in the correct directory project4 when you activate your virtual environemnt.

When everything is installed run cd into the project4 folder and run
```
python manage.py runserver 8080
```
then right click on the link at the bottom of your terminal.

Based on the SQL database that has been saved you can see other users posts and activity. Feel free to follow me in there ;)

## The future of this project
Unfortunately this project has no further use than the base case of learning and practicing new technologies. This project taught me the fundamentals of backend system, how to pull data using the Django framework API, data modeling with SQL, CRUD applications with SQL, and the fundamentals of SQL. This was the first of many small projects I have created over the years and it has taught me a lot.