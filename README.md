# Определение движения
Задание для самостоятельной работы:
Подключить 1 пироэлектрический датчик движения, 1 светодиод. При обнаружении движе-ния датчиком, включать светодиод и начинать прием изображения с камеры. При срабатывании дат-чика по видеопотоку определять, двигается ли человек. 

## Установка
Для работы программы к стандартному дистрибутиву python3 для Raspberry Pi необходимы установить следующие пакеты:
* sudo apg-get update && sudo apt-get upgrade
* sudo apt-get install build-essential cmake pkg-config cmake-curses-gui libgtk2.0-dev 
* sudo apt-get install libjpeg-dev libpng12-dev libtiff5-dev 
* sudo apt-get install libjasper-dev libavcodec-dev libavformat-dev 
* sudo apt-get install libswscale-dev libv4l-dev libx264-dev libxvidcore-dev 
* sudo apt-get install gfortran libatlas-base-dev
* sudo apt-get install python3-dev 
* sudo pip3 install numpy 
* sudo apt install python3-opencv opencv-python opencv-contrib-python

## Запуск
Из дериктории с файлом detector.py

`python3 sens.py`

## Содержимое директории
* `frozen_inference_graph.pb` - предобученная модель 
* `mobilenet_config.pbtxt` - конфигурационный файл 
* `sens.py` - код с запуском видеопотока по срабатыванию датчика без нейронной сети
* `check_button.py`  - код для проверки работы кнопки
* `check_led.py` - код для проверки работы LED и пироэлектродатчика
* `ckeck_opencv.py` - код для проверки работы OpenCV
* `check_servo.py`  - код для управления сервомотором (ШИМ)

Подробнее о файлах с предобученной моделью и конфигурации можно прочитать по ссылке https://github.com/opencv/opencv/wiki/TensorFlow-Object-Detection-API#use-existing-config-file-for-your-model

