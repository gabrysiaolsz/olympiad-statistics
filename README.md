#Installation and usage guide
First, create virtual environment, by running the following command: `$ python3 -m venv venv`

After that, activate it with: `$ source venv/bin/activate`

Then, download the requirements by running: `$ pip install -r requirements.txt`

Make and apply migrations with: `$ python manage.py makemigrations` `$ python manage.py migrate`

Finally, let's run the server: `$ python manage.py runserver`   

The output shows the URL where the app is being served in your local machine - it's the `localhost:8000`

#A little about the app
   - It shows different kind of statistics about the Olympic Games.
   - It was made for a university classes about databases.
