from celery import Celery, shared_task

import time

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@shared_task
def send_sms():
    print("Start send SMS task")
    time.sleep(10)
    print("Start send SMS task")
    return True
