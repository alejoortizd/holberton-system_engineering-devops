#!/usr/bin/python3

import csv
import requests
from sys import argv

if __name__ == '__main__':
    idU = argv[1]
    urlUser = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(idU)).json()
    listTodo = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'
        .format(idU)).json()
    with open('{}.csv'.format(idU), 'w', newline='') as csvfile:
        file = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for pending in listTodo:
            file.writerow([int(idU),
                           urlUser.get('username'),
                           urlUser.get('completed'),
                           urlUser.get('title')])
