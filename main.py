"""
Simple in-memory To Do List interactive application

This program will allow you to create, edit, end manage to-do list
as well to the task in it.
"""

from ToDoListPackage import tdl_manager

list_id = tdl_manager.create_new_list()

tdl_manager.create_new_task(list_id, "Finish the TP Wiki")

print(tdl_manager.get_all_lists())

print(tdl_manager.get_list(list_id))
