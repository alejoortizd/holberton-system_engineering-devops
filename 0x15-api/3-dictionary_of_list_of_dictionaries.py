#!/usr/bin/python3

import json
import requests

if __name__ == '__main__':
    urlUser = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    listTodo = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()

    users = {}
    usernames = {}
    for user in urlUser:
        idU = user.get('id')
        users[idU] = []
        usernames[idU] = user.get('username')

    for pending in listTodo:
        pendings = {}
        idU = pending.get('userId')
        pendings['task'] = pending.get('title')
        pendings['completed'] = pending.get('completed')
        pendings['username'] = usernames.get('idU')
        users.get(idU).append(pendings)
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(users, jsonfile)
