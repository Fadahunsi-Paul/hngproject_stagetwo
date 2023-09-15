# HNGx_task_two

A basic django Rest api capable of  performing CRUD operations 
## - Requirements
     To install the used packages run the command below
     pip install -r requirements.txt
## - Create Django Project,App and Virtual environment
      Run "django-admin startproject projectname" to create project
      Run "django-admin startapp appname" to create app
      Run "python -m venv namepofenvironment and activate it via "Scripts/activate
## - Configure Settings
      Save your app(appname) and rest_framework at the installed apps in the settings.py 
### - Define and Register Models
      Define your models at the models.py and register them at the admin.py
### - Create database by making Migrations
      Run "python manage.py makemigrations"
      Run "python manage.py migrate"
## - Create Your Api and View
     This is done at the views.py
### - Define your urls at the urls.py

## - Running Api :
         Run "python manage.py runserver"
  ## - Accessing the Api
       The Api is accessible at the local host(http//http://127.0.0.1:8000/api/)
  ## - Texting the Api
      The api can be tested with postman or python's 'request' library
  ## - Endpoints
      Determine the API endpoints defined in the URL patterns.
      The endpoints are the views and actions made in the  API
  ## - Http Methods
      The http methods used were(Get,Post,Put,Delete)
      Get(Read)      - To retrieve the api
      Post(Create)   - Used to create a new api
      Put(update)    - Used to make changes to the api
      Delete         - Used to remove an api
  ### - If no errors are determined after testing, the Api is valid.
        Host the api 
