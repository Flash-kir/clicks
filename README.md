# clicks

Программа запрашивает url адрес и возвращает короткую ссылку.
Если пользователь вводит короткую ссылку программа возвращает число переходов по ней за все время.

## install

Для установки компонентов выполните:

        pip install -r requirenments.txt

Перед запуском необходимо зарегистрироваться на http://bit.ly, получить GENERIC_ACCESS_TOKEN и поместить его в файл .env в папке проекта.

Для запуска:

        python main.py

## private variable

В файле .env в папке проекта хранится токен:

        BITLY_GENERIC_ACCESS_TOKEN = '{GENERIC_ACCESS_TOKEN}'
