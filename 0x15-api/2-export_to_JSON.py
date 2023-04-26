#!/usr/bin/python3

"""
This script retrieves information from a REST API to display the progress of an employee's TODO list.
It takes an employee ID as a command-line argument and displays the number of completed tasks
out of the total tasks, along with the titles of the completed tasks.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Args:
    employee_id (int): The ID of the employee

Returns:
    None
"""

import json
import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            emp_req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            task_req = requests.get('{}/todos'.format(REST_API)).json()
            emp_name = emp_req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, task_req))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))

            user_tasks = {"{}".format(id): []}
            for task in tasks:
                task_dict = {"task": task.get('title'),
                             "completed": task.get('completed'),
                             "username": emp_name}
                user_tasks["{}".format(id)].append(task_dict)

            filename = "{}.json".format(id)
            with open(filename, 'w') as f:
                json.dump(user_tasks, f)
