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


def create_new_task(list_id: str, title: str, task: str) -> str:
    """Add a new task to a specific list and return its ID."""
    try:
        new_id = generate_task_id(list_id)
    except KeyError:
        return None

    tdl[list_id][new_id] = {
        "Title": title,
        "Task": task
    }

    return new_id


def get_task(task_id: str) -> str:
    """Search and return the task with the given ID"""
    list_id = task_id.split("T")[0]

    try:
        return tdl[list_id][task_id]
    except KeyError:
        return None


def search_task(title: str = None, content: str = None) -> dict:
    """
    Search for a task matching the given title or task content.
    Return the task if found, else return None
    """
    if title is None and content is None:
        return None

    # Iterate all tasklists to find the one that meets the criteria
    for todo in tdl.values():
        for task in todo.values():
            # Check if the title was specified
            # Then check if the title is the one searched
            if title and title.lower() in task["Title"].lower():
                return task
            # Check if the content was specified
            # Then check if the content is the one searched
            if content and content.lower() in task["Task"].lower():
                return task

    return None


def update_task(task_id:  str, title: str = None, content: str = None) -> bool:
    """Modify an existing task by its ID"""
    list_id = task_id.split("T")[0]

    # Make sure that the ID is in the To Do List
    try:
        task = tdl[list_id][task_id]
    except KeyError:
        return False

    # There are no changes to make here
    if title is None and content is None:
        return False

    if title:
        task['Title'] = title

    if content:
        task['Task'] = content

    return True


def delete_task(task_id: str) -> bool:
    """Remove the task with the given ID"""
    list_id = task_id.split("T")[0]

    # Make sure that the ID is in the To Do List
    try:
        del tdl[list_id][task_id]
        return True
    except KeyError:
        return False
