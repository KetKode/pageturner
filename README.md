# WeRead book platform (backend)

### Stack:

- Django
- Django REST Framework
- PostgreSQL
- Celery (to be added)
- Docker
- Redis (to be added)

**API docs:** http://localhost:8000/api/docs/


### clone project repo

```
git clone https://github.com/KetKode/weread.git
```

### add .env like .env.example

```
POSTGRESQL_HOST=11.22.333.44
POSTGRESQL_PORT=5432
POSTGRESQL_USER=db_user
POSTGRESQL_PASSWORD=db_password
POSTGRESQL_DBNAME=db_name

SECRET_KEY=your_secret_key
```

### cd into working directory

```
cd pageturner
```

### run dev build

```
sudo docker compose docker-compose.yml up --build -d
```

### configure venv (if you need)

```
poetry env use python3.11
```
