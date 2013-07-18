django-startup-template
=======================

A Django 1.5.1 template to kickstart a new web app on a Webfaction server.

Features
========
Out of the box this project template provides the following packages and functionality:

1. Local and Production settings files.
2. django-storage: Static file storage on Amazon S3.
3. django-compress: Pre-process and Compress CSS & JavaScript.
4. django-debug-toolbar: Awesome tool to debug your django site locally.
5. south: Painless database schema migrations.

Requirements
=============

1. Git
2. Pip
3. virtualenv

Install
=======
**Create a new folder on your system and switch to that folder**

```
mkdir my_django_project
```


```
cd my_django_project
```

**Create and initialize a new virtual environment**

```
source /usr/local/bin/virtualenvwrapper.sh
```

You should probably change ```env_my_django_project``` to something more 
meaningful.

```
mkvirtualenv env_my_django_project
```

Acticate the virtual environment.

```
workon env_my_django_project
```

**Download and install the latest stable version of Django (1.4)**

```
pip install django
```

This may take a few minutes.

**Create a new Django project** using this repo as a project template and 
switch to the new application folder

```
django-admin.py startproject --template=https://github.com/rudasn/django-startup-template/zipball/master --extension=py,md,conf,.gitignore PROJECT_NAME; cd PROJECT_NAME
```

**Make sure you replace ``PROJECT_NAME`` with the name of your project**

Now browse to the new project's directory and follow the instructions in **SETUP.md**.
