# HNGx Backend Stage 2 Task: API Documentation

### Introduction

This API allows you to perform *CRUD (Create, Read, Update, Delete) operations* on user profiles.

## API Endpoints
#### Create a Person Profile
Endpoint: POST /api

##### Request Format:
`{
    "name": "Tulasi"
}`

##### Response Format:
    {
        "status": 200 ok,
       
         {
            "id": 1,
            "name": "Tulasi",
            "email": "t@gmail.com",
            "country": "CHAD"
        }

    }

#### Get Person Profile
Endpoint: GET /api/{user_id}

##### Request Format: 
`No request body required.`

##### Response Format:
    {
        {
            "id": 1,
            "name": "Tulasi",
            "email": "t@gmail.com",
            "country": "CHAD"
        }
    }

#### Update Person Profile
Endpoint: PUT /api/{user_id}

##### Request Format:
    {
        "name": "Updated Name"
        "email":"Updated Email"
        "country":"Updated Country"
    }

##### Response Format:
    {
        "status": 200 ok,
       
    }

#### Delete Person Profile
Endpoint: DELETE /api/{user_id}

##### Request Format: 
    No request body required.

##### Response Format:
    {
        "status": 204 No Content,
       
    }

## Sample Usage

### Creating a Person Profile
##### Request:

###### POST /api
    Content-Type: application/json

    {
        "name": "Tulasi"
    }

#### Response:
    HTTP/1.1 201 Created
    {
        "status": true,
       
        {
            "id":1,
            "name": "Tulasi",
            "email": "t@gmail.com",
            "country": "CHAD"
        }
    }

### Getting Personal Profile
#### Request:
`GET /api/1`
#### Response:
    HTTP/1.1 200 OK
    {
        "status": 200 OK,
        {   "id":1,
            "name": "Tulasi",
            "email": "t@gmail.com",
            "country": "CHAD"
        }
    }


# Limitations and Assumptions
*The API assumes that person profiles are identified by unique numeric IDs.
This documentation covers the basic functionality of the API and does not include advanced features like authentication and authorization as the project does not require that.*

## Local Setup

*To set up and run the API locally:*

- Clone the repository from GitHub.
- Install the required dependencies using `pip install -r requirements.txt`.
- Create and apply the database migrations using `python manage.py makemigrations` and `python manage.py migrate`.
- Run the development server with `python manage.py runserver`.

