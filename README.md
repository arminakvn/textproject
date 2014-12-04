textproject
===========
Flask framework, Postgres database, probably backbone front-end
### setup and requirements
install and setup a virtualenv/visrtualenv wrapper
install flask through `pip install flask` and setup a postgres `pip install psycopg2 Flask-SQLAlchemy Flask-Migrate`

save installed libraries to the requirements.txt file with `pip freeze > requirements.txt`

add os.environ variables to the virtualenv wrapper's postactivate file with `vi $VIRTUAL_ENV/bin/postactivate` then hit `i`, add lines `export APP_SETTINGS="config.DevelopmentConfig"` and 
`export APP_SETTINGS="config.DevelopmentConfig"`
then hit esc, the :wq to save and out. deactivate/workon the virtualenv

### database migrations
In order to run migrations initialize Alembic: `python manage.py db init`. this will create a new folder: migrations. create a migration with the migration command: `python manage.py db migrate`

