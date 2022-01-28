====
NYPL APP by Tim Payne
====

This sample app returns a random image from the NYPL Collections API based
on the day of creation. It's a little buggy... the date might be off sometimes
but you should get a fun image irregardless.

The main script lives in nypl_img/views.py.

User Guide
----------

1. Set up your Auth token. This app assumes you have a .env file containing
   TOKEN = 'Token token={your-token}'

2. Run the development server (manage.py runserver) on localhost http://127.0.0.1:8000/

3. navigate to /nypl_img/randomimg/

4. add a value of the form yyyy-mm-dd at the end of the url to generate a random image result!
