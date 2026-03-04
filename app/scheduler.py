import time

while True:
    runnable_tasks = get_tasks_ready_to_run()
    for task in runnable_tasks:
        send_to_queue(task)
        mark_as_QUEUED(task)
    time.sleep(5)
