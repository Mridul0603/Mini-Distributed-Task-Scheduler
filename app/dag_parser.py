def validate_dag(tasks):
    graph = {}
    indegree = {}

    for task in tasks:
        graph[task["task_id"]] = task["depends_on"]
        indegree[task["task_id"]] = len(task["depends_on"])

    queue = [t for t in indegree if indegree[t] == 0]
    visited = 0

    while queue:
        node = queue.pop(0)
        visited += 1
        for t in graph:
            if node in graph[t]:
                indegree[t] -= 1
                if indegree[t] == 0:
                    queue.append(t)

    return visited == len(tasks)
