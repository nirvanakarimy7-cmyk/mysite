set -o errexit
pip install -r requirements.txt
<<<<<<< HEAD
python manage.py migrate
=======
>>>>>>> 9e06aa39a9d1918b4e1bcb3e31f03b2c3b39c2b9
python manage.py collectstatic --noinput
