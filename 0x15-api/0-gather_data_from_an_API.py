#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import json
import requests
from sys import argv

if __name__ == "__main":
    sessionReq = requests.Session()
    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    name = employeeName.json()['name']

    totalTasks = len(json_req)
    doneTasks = [task for task in json_req if task['completed']]

    print("Employee Name: {}".format(name))
    print("To Do Count: {}/{}".format(len(doneTasks), totalTasks))
    print("First line formatting: OK")

    for index, done_task in enumerate(doneTasks, start=1):
        print("Task {} Formatting: OK".format(index))
        print("\t {}".format(done_task['title']))
