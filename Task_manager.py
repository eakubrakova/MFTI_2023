from collections import defaultdict, deque

def task_manager(tasks):
    task_dict = defaultdict(deque)
    for task in tasks:
        task_id, server, priority = task
        if priority:
            task_dict[server].appendleft(task_id)
        else:
            task_dict[server].append(task_id)
    return task_dict

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]
 
print(task_manager(tasks))