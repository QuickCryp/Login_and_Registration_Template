So, for the start, create virtual enviroment
```python -m venv venv```
Next, start vitrual enviroment
```venv\Scripts\Activate```
Then, install requirements.txt
```pip intall -r requrements.txt```
After this, make migrations for database
```python manage.py makemigrations```
```python manage.py migrate```
And, at the end, run the project
```python manage.py runserver```

Have a good day!
