# skoltech-test-task

### graph/utils.py
    Содержит класс Graph со всеми описанными методами:

+ А. Добавление узла с какой-то информацией.
+ Б. Добавление ребра между двумя графами;
+ B. Генерация случайного графа;
+ Г. Отрисовка получившегося графа с matplotlib.


### graph/testing.ipynb
    Написан алгоритм с использованием модуля Graph


### roket/roket.ipynb
    Три вида генерации ядер:
    1. Равномерное (нормальные) сэмплирование
    2. Бинарные значения
    3. Тернарные значения

### roket/*.csv
    Отчеты по запускам для каждого из ядер (короткий сэмпл; каждый семпл; усредненный по всем запускам)

### docker/Dockerfile
    Файл образа для запуска контейнера

### docker/*.sh
    Конфиги bash

### docker running
    docker build -t testimage . && \
    docker run -dit --name testtask -v $(pwd):/data testimage && \
    docker exec testtask /work/countword.sh /data/text.txt && \
    docker exec testtask /work/createfile.sh /data/text.txt /data/output