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
import requests


REST_API = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    emp_req = requests.get('{}/users'.format(REST_API)).json()
    task_req = requests.get('{}/todos'.format(REST_API)).json()

    todo_all_employees = {}

    for user in emp_req:
        emp_id = user.get('id')
        emp_username = user.get('username')
        emp_tasks = list(filter(lambda x: x.get('userId') == emp_id, task_req))

        todo_list = []
        for task in emp_tasks:
            task_dict = {
                "username": emp_username,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            todo_list.append(task_dict)

        todo_all_employees[emp_id] = todo_list

    with open('todo_all_employees.json', mode='w', encoding='utf-8') as file:
        json.dump(todo_all_employees, file)
