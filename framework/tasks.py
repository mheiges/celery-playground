from __future__ import absolute_import

from framework.celery import app


@app.task
def add(x, y):
  return x + y


@app.task
def mul(x, y):
  return x * y


@app.task
def xsum(numbers):
  return sum(numbers)