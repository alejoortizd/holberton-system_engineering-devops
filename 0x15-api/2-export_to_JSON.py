#!/usr/bin/python3

import json
import requests
from sys import argv

if __name__ == '__main__':
    idU = argv[1]
    urlUser = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(idU)).json()
    listTodo = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'
        .format(idU)).json()
    pendingList = []
    for pending in listTodo:
        pendingDict = {}
        pendingDict['task'] = pending.get('title')
        pendingDict['completed'] = pending.get('completed')
        pendingDict['username'] = urlUser.get('username')
        pendingList.append(pendingDict)
    jObject = {}
    jObject[idU] = pendingList
    with open('{}.json'.format(idU), 'w') as jsonfile:
        json.dump(jObject, jsonfile)
