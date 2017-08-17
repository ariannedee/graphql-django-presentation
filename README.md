### GraphQL and Django sample project (with Graphene!)

1. Clone or download the repo
2. cd into the django_site directory
3. Create a virtual env, `pip install -r requirements.txt`
4. `$ ./manage.py runserver`
5. Go to https://localhost:8000/graphql to start using the Graphiql interface
6. Play around with adding custom fields, filters, and more complex models.

To add more data, use the shell `$ ./manage.py shell` and create User, Objective, and KeyResult objects.

The default admin user is:
Username: admin
Password: a