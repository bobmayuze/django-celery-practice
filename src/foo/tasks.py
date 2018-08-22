# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from src.celery import app
import time


def bar():
    add.delay(2, 4)


@app.task
def add(x, y):
    time.sleep(5)
    return x + y


# @shared_task
# def mul(x, y):
#     return x * y

# @shared_task
# def xsum(numbers):
#     return sum(numbers)