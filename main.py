"""
Simple in-memory To Do List interactive application

This program will allow you to create, edit, end manage to-do list
as well to the task in it.
"""

from ToDoListPackage import tdl_manager, utils


print("""

 ███████████             ██████████               █████        ███           █████
░█░░░███░░░█            ░░███░░░░███             ░░███        ░░░           ░░███
░   ░███  ░   ██████     ░███   ░░███  ██████     ░███        ████   █████  ███████
    ░███     ███░░███    ░███    ░███ ███░░███    ░███       ░░███  ███░░  ░░░███░
    ░███    ░███ ░███    ░███    ░███░███ ░███    ░███        ░███ ░░█████   ░███
    ░███    ░███ ░███    ░███    ███ ░███ ░███    ░███      █ ░███  ░░░░███  ░███ ███
    █████   ░░██████     ██████████  ░░██████     ███████████ █████ ██████   ░░█████
   ░░░░░     ░░░░░░     ░░░░░░░░░░    ░░░░░░     ░░░░░░░░░░░ ░░░░░ ░░░░░░     ░░░░░

> Version: 0.1
> Author: Walter Saldaña
""")


menu = """
Select an option:
    1) Create a new empty todo list
    2) Add a new task to the list
    3) List all the current tasks
    4) List all todo lists
    5) Obtain a specific task by id
    6) Obtain a specific list by id
    7) Modify a specific task by id
    8) Delete a specific task
    9) Search for a task using its title
    10) Search task by contents
    11) Exit
> """


while True:
    option = input(menu)
    print("")

    if option == "1":
        # Create a new empty todo list
        list_id = tdl_manager.create_new_list()

        print(">> Done!")
        print(">> List ID: " + list_id)

    elif option == "2":
        # Add a new task to the list
        list_id = input('List ID: ')
        title = input('Task title: ')
        content = input('Task content: ')

        task_id = tdl_manager.create_new_task(list_id, title, content)

        if task_id is None:
            print("\n(!) List '" + list_id + "' not found.")
        else:
            print("\n>> Done!")
            print(">> Task ID: " + task_id)

    elif option == "3":
        # List all the current tasks
        print(">> Displaying all your current tasks\n")

        tdls = tdl_manager.get_all_lists()

        for v in tdls.values():
            utils.print_tasks(v)

    elif option == "4":
        # List all todo lists
        print(">> Displaying all your To-Do Lists\n")

        tdls = tdl_manager.get_all_lists()

        for k, v in zip(tdls.keys(), tdls.values()):
            print("* List: " + k)
            utils.print_tasks(v)

    elif option == "5":
        # Obtain a specific task by id
        task_id = input('Task ID: ')
        task = tdl_manager.get_task(task_id)

        if task is None:
            print("\n(!) We couldn't find a task with ID: " + task_id)
        else:
            print("\n>> " + task['Title'] + ": " + task['Task'])

    elif option == "6":
        # Obtain a specific list by id
        list_id = input('List ID: ')

        li = tdl_manager.get_list(list_id)

        if li is None:
            print("\n(!) We couldn't find a list with ID: " + list_id)
        else:
            print("\n* List: " + list_id)
            utils.print_tasks(li)

    elif option == "7":
        # Modify a specific task by id
        task_id = input('Task ID: ')
        task = tdl_manager.get_task(task_id)

        if task is None:
            print("\n(!) We couldn't find a task with ID: " + task_id)
        else:
            print("\n>> " + task['Title'] + ": " + task['Task'])

            print(">> Insert new values (press ENTER if no changes needed)")
            title = input('Task title: ')
            content = input('Task content: ')

            updates = tdl_manager.update_task(task_id, title, content)

            if updates:
                print("\n>> Done!")
            else:
                print("\n(!) Something went wrong...")

    elif option == "8":
        # Delete a specific task
        task_id = input('Task ID: ')
        task = tdl_manager.get_task(task_id)

        if task is None:
            print("\n(!) We couldn't find a task with ID: " + task_id)
        else:
            print("\n>> " + task['Title'] + ": " + task['Task'])
            print("(!) This can't be undone")
            confirm = input("(!) Are you sure you want to delete this task? (y/n): ")

            if confirm == "y":
                tdl_manager.delete_task(task_id)
                print("\n>> Task deleted")
            else:
                print("\n>> The task was not deleted")

    elif option == "9":
        # Search for a task using its title
        title = input('Task Title: ')
        task = tdl_manager.search_task(title=title)

        if task is None:
            print("\n(!) No task match with the title: " + title)
        else:
            utils.print_tasks({"Best match": task})

    elif option == "10":
        # Search task by contents
        content = input('Task content: ')
        task = tdl_manager.search_task(content=content)

        if task is None:
            print("\n(!) No task match with: " + content)
        else:
            utils.print_tasks({"Best match": task})

    elif option == "11":
        print(">> Have a nice day!")
        break

    else:
        print("(!) Please select a valid option...")
