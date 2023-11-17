all: delete-db migrate run

migrations:
	pipenv run python manage.py makemigrations quickstart

migrate: migrations
	pipenv run python manage.py migrate
    
run:
	pipenv run python manage.py runserver

delete-db:
	rm -rf quickstart/migrations
	rm db.sqlite3
