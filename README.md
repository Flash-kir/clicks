# Посчитайте клики по ссылкам

При запуске программы в качестве аргумента передаем url адрес и получаем короткую ссылку.
Если передать короткую ссылку, то программа возвращает число переходов по ней за все время.

## Установка

Клонируйте репозиторий:

    git clone git@github.com:Flash-kir/clicks.git

Для установки компонентов выполните:

    pip install -r requirenments.txt

Перед запуском необходимо зарегистрироваться на http://bit.ly, получить GENERIC_ACCESS_TOKEN и поместить его в файл .env в папке проекта.

Для запуска вызовите:

    python main.py [url]

аргумент url это короткая ссылка или url адрес

## Секретные переменные

В файле .env в папке проекта хранится токен:

    BITLY_TOKEN='{GENERIC_ACCESS_TOKEN}'
