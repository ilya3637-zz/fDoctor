# AutoTests for Weather API

Так же проект доступен в docker. Образ собран на macOS. 
В основе python3 https://hub.docker.com/_/python

Для использования - [загрузить контейнер](https://drive.google.com/file/d/1UQbjNRcsbYWkugeH5_st-9uzNg9j-845/view?usp=sharing) на устройство и выполнить в папке с архивом следующие команды:

$ docker load < myimage_latest.tar.gz

$ docker run my_test_app

Входят следующие тесты:
- проверка получения 200 кода + валидного json для текущей погоды в Москве
- проверка получения 200 кода + валидного json для истории погоды в Москве за последние 5 дней
