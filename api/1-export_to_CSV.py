#!/usr/bin/python3
"""
    data gathering from api module
    and exporting to a csv file
"""
import csv
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

# Export using csv format
with open('USER_ID.csv', 'w') as csvfile:
    # Ceating a csv writer object
    # Quoting=csv.QUOTE_ALL to quote all the fields
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for task in todo_data:
        # Writing the fields to the csv file
        writer.writerow([employee_id, employee_name, task['completed'],
                         task['title']])

if __name__ == '__main__':
    pass
