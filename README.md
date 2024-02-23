# django-translation-demo
A simple demo of the translation in django, both dynamic (db) and static text.


```bash
pip install Django==5.0.2
python3 manage.py migrate
python3 manage.py makemessages -l fr
python3 manage.py compilemessages
python3 manage.py runserver
# Now browse the site
http://127.0.0.1:8000/fr/dual-lang/dual_language/
http://127.0.0.1:8000/en/
```

create super user
```commandline
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@dcs.com', 'adminpass')" | python manage.py shell
```