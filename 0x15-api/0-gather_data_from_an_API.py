#!/usr/bin/python3
"""
Script to give the progress of an employee's TODO list
"""
import requests
import sys


# Base URL for the REST API
BASE_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    # Check if employee ID is provided as a command-line argument
    if len(sys.argv) == 2:
        employee_id = sys.argv[1]
        # Validate command-line argument for integer employee ID
        if employee_id.isdigit():
            get_employee_todo_progress(int(employee_id))
        else:
            print("Invalid employee ID. Please enter a valid integer.")
    else:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")


def get_employee_todo_progress(employee_id):
    """Get the employee information"""
    employee_info_url = f'{BASE_URL}/users/{employee_id}'
    employee_info = requests.get(employee_info_url).json()

    # Get employee's TODO list
    employee_todo_url = f'{BASE_URL}/todos?userId={employee_id}'
    employee_todo_list = requests.get(employee_todo_url).json()

    # Count the number of completed tasks
    completed_tasks = [
        task for task in employee_todo_list if task.get('completed', False)
    ]
    num_completed_tasks = len(completed_tasks)

    # Calculate the total number of tasks
    total_tasks = len(employee_todo_list)

    # Display employee TODO list progress
    print(f"Employee {employee_info['name']} is done with tasks"
          f"({num_completed_tasks}/{total_tasks}):")

    # Display completed tasks
    if num_completed_tasks > 0:
        for task in completed_tasks:
            print(f"\t\t{task['title']}")
