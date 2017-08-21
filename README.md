### GraphQL and Django+Graphene sample project

1. Clone or download the repo
2. Set up a virtual env
3. The django project is in the django_site directory. cd there and `pip install -r requirements.txt`
4. `$ ./manage.py runserver`
5. Go to http://localhost:8000/graphql to start using the Graphiql interface
6. Play around with adding custom fields, filters, and more complex models.

To add more data, use the shell `$ ./manage.py shell`, or go to the django admin (http://localhost:8000/admin) and create User, Objective, and KeyResult objects.

The default admin user is:
Username: admin
Password: a
