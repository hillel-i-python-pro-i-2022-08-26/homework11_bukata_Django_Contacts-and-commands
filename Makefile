.PHONY: homework-i-run
# Run homework.
homework-i-run:
	@python manage.py runserver # sign @ use for not show text of this command

.PHONY: homework-i-purge
# Delete all created artifacts, related with homework execution
homework-i-purge:
	@echo Goodbye # sign @ use for not show text of this command


.PHONY: init-dev
# Init environment for development
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install


.PHONY: pre-commit-run
# Run tools for files from commit.
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
# Run tools for all files.
pre-commit-run-all:
	@pre-commit run --all-files

.PHONY: migrations
# Make migrations
migrations:
	@python manage.py makemigrations

.PHONY: migrate
# Migrate
migrate:
	@python manage.py migrate

.PHONY: init-dev-i-create-superuser
init-dev-i-create-superuser:
	@DJANGO_SUPERUSER_PASSWORD=admin123 python manage.py createsuperuser --user admin --email admin@gmail.com --no-input

# in this command : command python manage.py createsuperuser: to create user with its own pevilagies
# then --user admin login of the user (now: admin)
# email of user: --email admin@gmail.com
#  --no-input: non intaractive command (not to be ask by pycharm: name of user, his email and password
#in this case command will be implam without questions
# admin123: password which we give to variable environment
# @DJANGO_SUPERUSER_PASSWORD: variable environment