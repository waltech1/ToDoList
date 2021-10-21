"""
Simple in-memory To Do List interactive application

This program will allow you to create, edit, end manage to-do list
as well to the task in it.
"""

from ToDoListPackage import tdl_manager

list_id = tdl_manager.create_new_list()

task_id = tdl_manager.create_new_task(
    list_id,
    "Finish the TP Wiki",
    "Read all the documentations and watch all the videos"
)

print(tdl_manager.get_all_lists())

print(tdl_manager.get_list(list_id))

print(tdl_manager.get_task(task_id))

print(tdl_manager.search_task("wiki"))

print(tdl_manager.update_task("k", "Do the TP Wiki"))
print(tdl_manager.update_task(task_id, content="Read all the docs and watch all the tutorials"))

print(tdl_manager.get_task(task_id))