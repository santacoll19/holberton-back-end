#!/usr/bin/python3
"""
    data gathering from api module
"""
import json
import requests
import sys


# python3 0-gather_data_from_an_API.py 2 is the run command where two is the id
employee_id = sys.argv[1]

# uses request import to get the data from the api
user_response = requests.get(
    'https://jsonplaceholder.typicode.com/users/' + employee_id)

# converts the data to json format
data = user_response.json()

# gets the name of the employee
employee_name = data['name']

# gets the tasks of the employee
todo_response = requests.get(
    'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id)

# converts the tasks data to json format
todo_data = todo_response.json()

# gets the total number of tasks
todo_total = str(len(todo_data))

# gets the number of completed tasks
todo_completed = str(sum(1 for task in todo_data if task['completed']))

# prints the data in the format required
print('Employee {} is done with tasks({}/{}):'.format(employee_name,
      todo_completed, todo_total))

# prints the completed tasks by title of task
for task in todo_data:
    if task['completed']:
        print('\t {}'.format(task['title']))

# Export using json format
with open('USER_ID.json', 'w') as jsonfile:
    json.dump({employee_id: [{
        "task": task['title'],
        "completed": task['completed'],
        "username": employee_name
    } for task in todo_data]}, jsonfile)

if __name__ == '__main__':
    pass
