from celery import Celery, Task
from dotenv import load_dotenv
import os
from controller.saveResultToFile import saveResultToFile

load_dotenv()
RABBITMQ_USER = os.getenv("RABBITMQ_USER")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")
RABBITMQ_VHOST = os.getenv("RABBITMQ_VHOST")

app = Celery(
    'tasks',
    broker = f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@localhost:5672/{RABBITMQ_VHOST}'
)

class FibonacciTask(Task):
    def on_success(self, result, task_id, args, kwargs):
        print(result)
        saveResultToFile(task_id, result)

@app.task(base=FibonacciTask)
def fibonacci(n):
    if n <= 0:
        return False
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



