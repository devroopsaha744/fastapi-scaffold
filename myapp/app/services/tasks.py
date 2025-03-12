from fastapi import BackgroundTasks
import uuid
from app.logger import logger

def send_email(email: str):
    logger.info(f'Sending email to {email}')
    return True

def process_background_task(bg_tasks: BackgroundTasks, task_function, *args, **kwargs):
    task_id = str(uuid.uuid4())
    def _run():
        task_function(*args, **kwargs)
    bg_tasks.add_task(_run)
    return task_id
