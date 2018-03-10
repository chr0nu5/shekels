# shekels
A very simple and fast finance manager made in Python.

# running

Open the shell:

```
docker-compose build api
docker-compose up api
```

In another shell:

```
docker-compose exec db bash
psql -U postgres
create database api;
\q
exit
```

Then:

```
docker-compose exec api bash
./manage.py test
./manage.py migrate
./manage.py createsuperuser
```

Back to the first shell, press CTRL+C and then:

```
docker-compose up api
```

Go to:

```
http://localhost:9000/
```

🖖 Enjoy!
