# AutoTests for Weather API

Образ собран на macos 
В основе pytho3 https://hub.docker.com/_/python

Для использования - загрузить контейнер на устройство.
$ docker load < myimage_latest.tar.gz
$ docker run my_test_app

Входят следующие тесты:
- проверка получения 200 кода + валидного json для текущей погоды в Москве
- проверка получения 200 кода + валидного json для истории погоды в Москве за последние 5 дней
