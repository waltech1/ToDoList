"""
This contains some useful functions to manage
better the to-do list items.
"""

__version__ = '0.1'
__author__ = 'Walter Saldaña'


def get_list_titles(task: dict, id: str) -> str:
    """
    Return only the title from a task.

    This functions is used to map a to-do list
    with only the titles of its tasks.
    """
    return "("+id+") " + task['Title'] + ": " + task['Task']


def print_tasks(task: dict):
    """
    Iterate over a To-Do list and print each of its tasks.
    """
    tasks_values = list(map(get_list_titles, task.values(), task.keys()))

    for task in tasks_values:
        print("  - " + task)
