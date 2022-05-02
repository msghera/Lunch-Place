# Lunch Place
## _A simple Rest application to vote for a lunch place_

## Features
| Endpoint      | Description |
| ----------- | ----------- |
| _http://localhost:8000/auth/register/_| Employee Registration |
| _http://localhost:8000/auth/login/_ | Registered employee and admin can login (jwt based authentication used)        |
| _http://localhost:8000/restaurant/_| Can see all the restaurants |
| _http://localhost:8000/restaurant/add/_ | Admin can add restaurants     |
| _http://localhost:8000/restaurant/menu/_| Can see all the menus |
| _http://localhost:8000/restaurant/menu/add/_ | Admin can add menus     |
| _http://localhost:8000/poll/_| Can see all the choices for today |
| _http://localhost:8000/poll/start/_ | Admin can start the poll for today    |
| _http://localhost:8000/poll/vote/_ | Admin/Employee can vote for their favorite menu    |
| _http://localhost:8000/poll/end/_ | Admin can end the poll for today and winner restaurant will be found. No restaurant can be winner for 3 consecutive polls    |


- Import a HTML file and watch it magically convert to Markdown
- Drag and drop images (requires your Dropbox account be linked)
- Import and save files from GitHub, Dropbox, Google Drive and One Drive
- Drag and drop markdown and HTML files into Dillinger
- Export documents as Markdown, HTML and PDF

## Installation

## The Docker Way
0. Check if the postgres connectivity is non-commented and set according to your system.
1. Clone the repo `git clone git@github.com:msghera/Lunch-Place.git`
2. Move into the folder `cd Lunch-Place`
3. `sudo docker-compose build`

## The Manual Way
0. sqlite3 is default database here.
1. Clone the repo `git clone git@github.com:msghera/Lunch-Place.git`
2. Move into the folder `cd Lunch-Place`
3. You may create a virtual environment and use it 
```
python3 -m venv venv
source venv/bin/activate
```
4. run server in lunch_place folder `python3 manage.py runserver`

## Super User
Make sure for both approach you have created a superuser
`python manage.py createsuperuser`