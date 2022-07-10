import json
import requests
import configparser
from docs import path
import packages.todo.task as task


config = configparser.ConfigParser()
# Config for localhost.
config.read(path.PATH_CONFIG)

h_close = {'Connection': 'Close'}
h_content = {'Content-Type': 'application/json'}


def show_ToDoList(json: json):
    """Function to output result from JSON.

    Args:
        json (list): JSON list

    Returns:
        str: Result in the required form.
    """
    if json == []:
        print('\nToDoList is empty.')
    else:
        for task in json:
            # Output the result in the required form.
            print(f'''\nTask number: {task['id']}
            Day of the week: {task['day_week']}
            Task name: {task['name_task']}
            A priority: {task['prior']}
            Date and time of creation: {task['date_time']}''')


def task_get():
    """Function to get data from JSON.

    Returns:
        function show_ToDoList
    """
    try:
        reply = requests.get(config['db']['host'])
        close_conn()
    except requests.RequestException:
        print('Communication Error')
    else:
        # Сall the function to display the result if the server code is 200.
        if reply.status_code == requests.codes.ok:
            show_ToDoList(reply.json())
        elif reply.status_code == requests.codes.not_found:
            print('Resourse not found')
        else:
            print('Server Error')


def post_task(new_task: str):
    """Function to add data to JSON.

    Args:
        new_task (dict): Accepts a dictionary for JSON.
    """
    try:
        reply = requests.post(
            config['db']['host'], headers=h_content, data=json.dumps(new_task))
        close_conn()
    except requests.RequestException:
        print('Communication Error')
    else:
        # # Print result if the server code is 201.
        if reply.status_code == requests.codes.created:
            print('Task in JASON added successfully!')
        elif reply.status_code == requests.codes.not_found:
            print('Resourse not found')


def put_task(id: int, where_change: str, what_change: str):
    """Function to change data in JSON.

    Args:
        id (int): Number of task.
        where_change (str): Where there will be changes in the task, 1 - day of the week, 2 - priority.
        what_change (str): The value of the change.
    """
    try:
        # Getting a dictionary from the server by id.
        reply = requests.get(config['db']['host'] + '/' + str(id))
        dict_to_change = reply.json()
        # Change the dictionary and send the result.
        if where_change == '1':
            dict_to_change["day_week"] = what_change
            reply = requests.put(config['db']['host'] + '/' + str(id),
                                 headers=h_content, data=json.dumps(dict_to_change))
        elif where_change == '2':
            dict_to_change["prior"] = what_change
            reply = requests.put(config['db']['host'] + '/' + str(id),
                                 headers=h_content, data=json.dumps(dict_to_change))
        close_conn()
    except requests.RequestException:
        print('Communication Error')
    else:
        # Print result if the server code is 200.
        if reply.status_code == requests.codes.ok:
            print('Task in JASON changed successfully!')
        elif reply.status_code == requests.codes.not_found:
            print('Resourse not found')


def delete_task(id: int):
    """Function to remove data from JSON.

    Args:
        id (int): Number of task to delete.
    """
    try:
        reply = requests.delete(config['db']['host'] + '/' + str(id))
        close_conn()
    except requests.RequestException:
        print('Communication Error')
    else:
        # Print result if the server code is 200.
        if reply.status_code == requests.codes.ok:
            print('Removal from JSON completed successfully!')
        elif reply.status_code == requests.codes.not_found:
            print('Resourse not found')


def close_conn():
    """Function to close the connection to the server.
    """
    reply = requests.get(config['db']['host'], headers=h_close)
