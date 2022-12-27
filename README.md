# brighthotel
это вебсайт отеля с вожможностью бронирования номеров, регистрации и аутентификации пользователей, отправки отзывов, комментировать посты и т.д.

![Screenshot](https://user-images.githubusercontent.com/116701462/209672451-94193f5c-c09c-4b18-906c-12060c9b3fc8.png)

## Сборка репозитория и локальный запуск
**Выполните следующие команды в консоли**     
- Для клонирования проекта:

```git clone https://github.com/Geniuss87/brighthotel.git```

- Для установки виртуального окружения (пердварительно перейти в директорию проекта):

`python3 -m venv {название}` 

- Для активации виртуального окружения:

`source {название}/bin/activate`

- Для установки зависимостей:

`pip install -r requirements.exe`

## Настройка
Создайте файл .env и добавьте следующие настройки:   
`SECRET_KEY=django-insecure-@jysfta(f(6o4$^$xe)ukm)3p16)xqy$#p350_0rz^vb9g_b(3`   
`DEBUG=True`   
`ALLOWED_HOSTS=127.0.0.1, localhost`   
`ENGINE=django.db.backends.postgresql`   
`NAME=hotel_db`   
`USR=postgres`   
`PASSWORD=postgres`   
`HOST=127.0.0.1`   
`PORT=5432`   

## Создание и наполнение базы данных
- Создайте в postgres базу данных hotel_db

- Сделайте миграцию выполнив следующие команды:

`./manage.py makemigrations`  
`./manage.py migrate`

## Создание суперпользователя и запуск сервера
- Для создания суперпользователя выполните следующую команду:

`./manage.py createsuperuser`

- В конце запускаем Сервер командой:

`./manage.py runserver`

### _После успешного запуска сервера, необходимо заполнить таблицы Room, Blog для полноценной функциональности сайта_
