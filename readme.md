# Home work 09

Long-running tasks з Celery

## Розгортаня проекту (команди для Windows)

1. Ініціалізувати GIT, склонувати репозиторій та перейти до деректорії локального репозиторію
    ```bash
    git init
    git clone https://github.com/AtamanAA/hillel_py_pro_home_work_09
    cd hillel_py_pro_home_work_09
    ```
2. Встановити venv та активувати його
    ```bash
    python -m venv venv
   .\venv\Scripts\activate    
    ```
3. Інсталювати сторонні пакети у venv
    ```bash
    python -m pip install -r requirements.txt    
    ```
4. Перейти до дерикторії проекту
    ```bash
    cd long_task_project    
    ```
5. Створити файл "**.env**" у головній деректорії проекту (поряд з файлом manage.py) і додати до нього запис зі своїм секретним токеном для Twilio як в прикладі нижче:
      
    ```
   TWILIO_AUTH_TOKEN = "adcd43qwerty....."   
    ```
6. Для запуску процессу [RabbitMQ](https://www.rabbitmq.com) в окремому терміналі виконати команду (переконатися що [Docker Desktop](https://www.docker.com/products/docker-desktop/) запущений )
    ```bash
    docker run -d -p 5672:5672 rabbitmq    
    ```
7. У окремому терміналі перейти до деректорії проекту та запустити процесс [Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)
    ```bash
    cd hillel_py_pro_home_work_09\long_task_project
    celery -A long_task_project worker -l INFO    
    ```
8. Повернутися до першого терміналу (де активоване venv) та виконати запуск основного web-серверу
    ```bash
    python manage.py runserver   
    ```
9. В браузері перейти на сторінку верефікації
    http://127.0.0.1:8000/verification/
