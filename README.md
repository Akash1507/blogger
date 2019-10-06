# Blogger - A Basic Blog Application Build with Django

## About

This is a simple Blog App where an authenticated user can post/edit/delete Blog Posts.

It was made using **Python 3.6** + **Django** and the database is **SQLite**.
**Bootstrap and Materialize CSS** were used for styling.


There is a login and registration functionality included.

The user has his own blog page, where he can add new blog posts.
The home page is paginated list of all posts.



## Prerequisites

\[Optional\] Install virtual environment:

```bash
$ python -m virtualenv env
```

\[Optional\] Activate virtual environment:

On macOS and Linux:
```bash
$ source env/bin/activate
```

On Windows:
```bash
$ .\env\Scripts\activate
```

Install dependencies:
```bash
$ pip install -r requirements.txt
```

## How to run

### Default

You can run the application from the command line with manage.py.
Go to the root folder of the application.

Run migrations:
```bash
$ python manage.py migrate
```


Run server on port 8000:
```bash
$ python manage.py runserver 8000
```





## Post Installation

Go to the web browser and visit `http://localhost:8000`

Register yourself or login if already registered

### Django Admin

It is possible to add additional admin users who can login to the admin site. Run the following command:
```bash
$ python manage.py createsuperuser
```
Enter your desired username and press enter.
```bash
Username: admin_username
```
You will then be prompted for your desired email address:
```bash
Email address: admin@example.com
```
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
```bash
Password: **********
Password (again): *********
Superuser created successfully.
```

Go to the web browser and visit `http://localhost:8000/admin`