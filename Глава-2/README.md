# Код из 2-главы книги "Django for API. Build web APIs with Python and Django. William S. Vincent" 

## Настройка перед запуском

Первое, что нужно сделать, это клонировать репозиторий:
```sh
$ git clone https://github.com/jumabekova06/Code-of-DjangoApiBook.git
$ cd Code-of-DjangoApiBook
$ cd Глава-2

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



