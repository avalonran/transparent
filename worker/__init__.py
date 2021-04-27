import os
from celery import Celery


#设置环境变量，加载django Setttings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transparent.settings')

#创建celery应用
celery_app = Celery('transparent')
celery_app.config_from_object('worker.config')
celery_app.autodiscover_tasks()


def call_by_worker(func):
    '''异步调用celery '''
    task = celery_app.task(func)
    return task.delay
