#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
   returns information about his/her TODO list progress
"""
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(sys.argv[1])).json()
    tasks = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed_tasks = [task.get("title") for task in tasks
                       if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed_tasks), len(tasks)))

    [print("\t {}".format(task)) for task in completed_tasks]
