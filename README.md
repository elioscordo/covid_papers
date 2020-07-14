# JSON Rest API for covid-19 related papers

A small demo project that exposes covid-19 related publications throught a rest API

# How to run the backend

Python 3 is required.

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py runserver localhost:<port>`

# How to run the app tests

`python manage.py test papers`

# How to use the api

Please refer to the browsable version of the api for usage.
The browsable api is available at the url `localhost:<port>`

# How to used the admin.
Create a super user to access the admin functionality

`python manage.py createsuperuser`

The admin is available at the url `localhost:<port>/admin/`

# How to import  a csv

Import csv from the shell:

`python manage.py shell`

`>>> import tablib`

`>>> from import_export import resources`

`>>> from papers.admin import PaperResource`

`>>> dataset =  tablib.Dataset().load(open('metadata.csv').read(), format='csv')`

`>>> result = PaperResource().import_data(dataset, dry_run=False, raise_exceptions=True)`

Import csv from the admin is experimental and it is provided under a few limitations.

The admin file upload and the confirmation page (see screeshots) make the admin tool slow and suitable for the following use cases:

 1) Small files with lessthan 1000 rows 
 2) Since only unchanged rows are not updated, corrected versions of an already iported database will work. 


