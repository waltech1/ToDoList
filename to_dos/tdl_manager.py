"""
This module is an implementation of a To Do List manager.

It can make CRUD operations over a dictionary being used as a To Do List.
"""

__version__ = '0.1'
__author__ = 'Walter Saldaña'


# Declare an empty dict to store the To-Do Lists
lists_db = {}


def get_all_lists() -> dict:
    """Return all the To Do Lists"""
    return lists_db


def get_list(list_id: str) -> dict:
    """Return the specified To Do List by its ID"""
    try:
        return lists_db[list_id]
    except KeyError:
        return None


def generate_list_id() -> str:
    """Create an ID for a new list."""
    n = len(lists_db) + 1
    return 'L' + str(n)


def generate_task_id(list_id: str) -> str:
    """Create an ID for a new task"""
    n = len(lists_db[list_id]) + 1

    return list_id + 'T' + str(n)


def create_new_list() -> str:
    """Add a new list to the manager and return its ID."""
    new_id = generate_list_id()
    lists_db[new_id] = {}

    return new_id


def create_new_task(list_id: str, title: str, task: str) -> str:
    """Add a new task to a specific list and return its ID."""
    try:
        new_id = generate_task_id(list_id)
    except KeyError:
        return None

    lists_db[list_id][new_id] = {
        "Title": title,
        "Task": task
    }

    return new_id


def get_task(task_id: str) -> str:
    """Search and return the task with the given ID"""
    list_id = task_id.split("T")[0]

    try:
        return lists_db[list_id][task_id]
    except KeyError:
        return None


def search_task(title: str = None, content: str = None) -> dict:
    """
    Search for a task matching the given title or task content.

    Return the task if found, else return None.
    The first matching criteria is the title (if it's provided),
    else, it's going to compare the content (if it's provided).
    If the user didn't provide a title nor content, it'll return None.

    Optional keyword arguments:
    title -- the title of the searched task (default None)
    content -- the content of the searched task (default None)
    """
    if title is None and content is None:
        return None

    # Iterate all tasklists to find the one that meets the criteria
    for todo in lists_db.values():
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
    """Modify an existing task by its ID.

    Searchs for a task given its ID to modify its title, content, or both.
    If no title or content is provided (None), it won't make any change
    to the task.

    Optional keyword arguments:
    title -- the new title for the task (default None)
    content -- the new content/description for the task (default None)
    """
    list_id = task_id.split("T")[0]

    # Make sure that the ID is in the To Do List
    try:
        task = lists_db[list_id][task_id]
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
        del lists_db[list_id][task_id]
        return True
    except KeyError:
        return False
