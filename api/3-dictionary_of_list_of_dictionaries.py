#!/usr/bin/python3
"""
    dictionary of list of dictionaries module
"""
import json
import requests

users = requests.get('https://jsonplaceholder.typicode.com/users').json()

todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

user_dict = {}

# loop to make id dictionary
for user in users:
    user_id = user.get('id')
    user_dict[user_id] = []
    # loop to make task dictionary
    for task in todos:
        if user_id == task.get('userId'):
            user_dict[user_id].append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': user.get('username')
            })

with open('todo_all_employees.json', 'w') as jsonfile:
    json.dump(user_dict, jsonfile)


if __name__ == '__main__':
    pass
