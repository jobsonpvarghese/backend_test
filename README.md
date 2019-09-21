# Asthra Management
Inorder to run this blog create a virtual enviornment and install all the required libraries.
## Steps

 
#### 1.Creating the virtual enviornment

    virtualenv Asthra
#### 2.Activating the virtual enviornment

    cd Asthra
    ./Scripts/activate
the above command is used on windows
#### 3.Cloning the Repository

    git clone https://github.com/jobsonpvarghese/backend_test.git
#### 4.Installing the required libraries

    cd backend_test
    pip install -r requirements.txt
#### 5.Applying the database migrations
This migrations are done inorder to create database tables depending on the model used

    python manage.py makemigrations
    python manage.py migrate
#### 6.Creating a Superuser
Inoreder to access the admin panel a superuser account is necessary 

    python manage.py createsuperuser
#### 7.Running The Server

    python manage.py runserver

