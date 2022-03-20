SkillCloud backend


Deployment as follows:

Django:
include SECRET_KEY in .env file

Persistent data storage
PostgreSQL:
sudo systemctl start postgresql
include DB credentials in .env file

Cache/message queue
Redis:
sudo systemctl start redis
include Redis credentials in .env file

start by:
make run_gunicorn
