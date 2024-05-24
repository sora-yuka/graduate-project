# RUNNING PROJECT
r:
	./manage.py runserver

# MAKING MIGRATIONS
m:
	./manage.py makemigrations
	./manage.py migrate

# TESTING APPLICATION
ta:
	./manage.py test apps.account.tests
tp:
	./manage.py test apps.profiles.tests

# CREATING ADMIN ACCOUNT
su:
	./manage.py createsuperuser

# STARTING CELERY
c:
	celery -A config worker -l info

# WRITING REQUIREMENTS
req:
	pip freeze > requirements.txt

d:
	docker-compose up --build