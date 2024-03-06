# Note Taking APIs
This repository contains the API endpoints for managing notes.

## Requirements
Python 3.x \
Django \
Django REST Framework \
Installation\

## Clone the repository:
```
git clone <repository_url>
```
## Create a virtual environment
```
python -m venv venv
```
## Active the env 
```
.\venv\Script\active.ps1
```
or for *Mac*
```
souce venv/bin/activate
```
## Install dependencies:
```
pip install -r requirements.txt
```
## Run migrations:
```
python manage.py migrate
```


## Usage
Start the Django development server:
```
python manage.py runserver
```
Access the API endpoints using a REST client like Postman or cURL.
## API Endpoints
`GET /notes/{note_id}/`: Retrieves a single note object that has id=note_id.\
`PUT /notes/{note_id}/`: Updates a single note object that has id=note_id.\
`GET /notes/?title=example`: Retrieves a list of all notes. Optionally, accepts query parameters for filtering notes by title.\
`POST /notes/`: Creates a new note.
## Required and optional Rarameters
```title``` : required for `POST`/optional for `PUT`
```body``` : required for `POST`/optional for `PUT`
