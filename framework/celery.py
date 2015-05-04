from __future__ import absolute_import

from celery import Celery

app = Celery('framework',
             include=['framework.tasks'])

app.config_from_object('framework.celeryconfig')

# Optional configuration, see the application user guide.
app.conf.update(
  CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
  app.start()
