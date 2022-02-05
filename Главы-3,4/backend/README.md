# Код из 2-главы книги "Django for API. Build web APIs with Python and Django. William S. Vincent" 

## Настройка перед запуском

Первое, что нужно сделать, это cклонировать репозиторий:
```sh
$ git clone https://github.com/jumabekova06/Code-of-DjangoApiBook.git
$ cd Code-of-DjangoApiBook
$ cd Глава-3
$ cd backend

```

Создайте виртуальную среду для установки зависимостей и активируйте ее:

```sh
$ virtualenv venv
$ source venv/bin/activate
```

Затем установите зависимости:

```sh
(venv)$ pip install -r requirements.txt
```
Запускаем сервер:
```sh

(venv)$ python manage.py runserver
```
навигация для API `http://127.0.0.1:8000/api/`.

навигация для детальной информации об объекте `http://127.0.0.1:8000/api/1`.

но прежде чем просматривать API,создайте суперпользователя
и зайдите в админку,затем создайте несколько объектов todo :

```sh

(venv)$ python manage.py createsuperuser

путь к админке `http://127.0.0.1:8000/admin/`.

```


