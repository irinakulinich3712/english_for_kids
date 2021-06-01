# English Courses website

## Setup

In order to run this project locally, follow these steps:

First of all, clone the repository:

```sh
git clone https://github.com/irinakulinich3712/english_for_kids.git
cd english_for_kids
```

Create a virtual environment to install dependencies in and activate it:

```sh
virtualenv2 --no-site-packages env
source env/bin/activate
```

Then install the dependencies:

```sh
(env) pip install -r requirements.txt
```
Once `pip` has finished downloading the dependencies:
```sh
(env) cd project
(env) python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
