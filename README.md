# chat-application

### create virtual environment
```
python -m venv env
```

### activate virtual environment
linux 
```bash
source env/bin/activate
```

windows
```bash
env\Scripts\activate
```

### install packages
```bash
pip install -r requirements.txt
```

### execute models
```bash
python manage.py makemigrations
python manage.py migrate
or
python manage.py makemigrations <appname>
python manage.py migrate <appname>
```

### run project
```bash
python manage.py runserver