# English Courses website

## Setup

Some of the project's configurations differ in the production version.
In order to run this project locally, follow these steps:

First of all, clone the repository:

```sh
git clone https://github.com/irinakulinich3712/english_for_kids.git
cd english_for_kids
```

Create a virtual environment to install dependencies in and activate it:

```sh
python -m venv venv
source venv/bin/activate
```
Put the your .env file in the root of the project.

In the settings.py change the following variables to this:

```sh
DEBUG = True

ALLOWED_HOSTS = []

```

Also, either set the CSRF_COOKIE_SECURE , SESSION_COOKIE_SECURE, SECURE_SSL_REDIRECT, SECURE_BROWSER_XSS_FILTER, SECURE_CONTENT_TYPE_NOSNIFF 
values to False or comment them

Also, in addStudentToGroup.js file change the urls in
```sh
const res = await fetch('https://www.englishforkids.com.ua/choose-student/');
```
and 
```sh
 const res = await fetch(`https://www.englishforkids.com.ua/groups/${groupId}/students/add-student/${studentId}/`);
```
to these, correspondingly:
```sh
const res = await fetch('http://127.0.0.1:8000/choose-student/');
const res = await fetch(`http://127.0.0.1:8000/groups/${groupId}/students/add-student/${studentId}/`);
```

Then install the dependencies:

```sh
(env) pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(env) python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
