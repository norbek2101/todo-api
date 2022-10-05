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


### websocket urls
ws://localhost:8000/chat/?token=<access_token>

### chat consumer action
{
    "action": "get-messages",
}

{
    "action": "send-message",
    "chat": <int:chat_number>,
    "text": "some text"
}

{
    "action": "get-message",
    "id": <int:message_id>
}

{
    "action": "update-message",
    "id": <int:message_id>,
    "text": "some text"
}

{
    "action": "delete-message",
    "id": <int:message_id>
}
