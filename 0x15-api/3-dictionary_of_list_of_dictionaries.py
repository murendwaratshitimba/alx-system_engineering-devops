#!/usr/bin/python3
'''
A script to export data in the JSON format
'''
import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    us = requests.get(url, verify=False).json()
    usernames = {}
    users = {}
    for user in us:
        uid = user.get("id")
        users[uid] = []
        usernames[uid] = user.get("username")
    url = "https://jsonplaceholder.typicode.com/todos"
    task = requests.get(url, verify=False).json()
    [users.get(t.get("userId")).append({"task": t.get("title"),
                                       "completed": t.get("completed"),
                                       "username": usernames.get(
                                               t.get("userId"))})
     for t in task]
    with open("todo_all_employees.json", 'w') as text:
        json.dump(users, text)
