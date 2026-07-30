from celery import shared_task

@shared_task
def send_task_creation_notification(task_priority, task_title):
    print(f'Task was created- Priority: {task_priority}, Task name: {task_title}') 