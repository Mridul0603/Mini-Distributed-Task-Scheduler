from celery import Celery

celery = Celery(
    "app",
    broker="redis://localhost:6379/0"
)

@celery.task(name="app.tasks.execute_task")
def execute_task(task_id):
    print(f"Running task {task_id}")