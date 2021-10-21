"""
This module is an implementation of a To Do List manager.

It can make CRUD operations over a dictionary being used as a To Do List.
"""

__version__ = '0.1'
__author__ = 'Walter Saldaña'

# Declare an empty dict to store the tasks
tdl = {}


def get_all_lists() -> dict:
    """Return all the To Do Lists"""
    return tdl


def get_list(list_id: str) -> dict:
    """Return the specified To Do List by its ID"""
    return tdl[list_id]


def generate_list_id() -> str:
    """Create an ID for a new list."""
    n = len(tdl) + 1
    return 'L' + str(n)


def generate_task_id(list_id: str) -> str:
    """Create an ID for a new task"""
    n = len(tdl[list_id]) + 1

    return list_id + 'T' + str(n)


def create_new_list() -> str:
    """Add a new list to the manager and return its ID."""
    new_id = generate_list_id()
    tdl[new_id] = {}

    return new_id


def create_new_task(list_id: str, task: str) -> str:
    """Add a new task to a specific list and return its ID."""
    new_id = generate_task_id(list_id)
    tdl[list_id][new_id] = task

    return new_id


def get_task(task_id: str) -> str:
    """Search and return the task with the given ID"""
    list_id = task_id.split("T")[0]

    return tdl[list_id][task_id]
