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
