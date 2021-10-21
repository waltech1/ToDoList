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

        print("\n>> Done!")
        print(">> Task ID: " + task_id)

    elif option == "3":
        # List all the current tasks
        print(">> Displaying all your current tasks\n")
        
        tdls = tdl_manager.get_all_lists()
        
        for v in tdls.values():
            tasks_values = list(map(utils.get_list_titles, v.values(), v.keys()))

            for task in tasks_values:
                print("  - " + task)

    elif option == "4":
        # List all todo lists
        print(">> Displaying all your To-Do Lists\n")

        tdls = tdl_manager.get_all_lists()
        
        for k, v in zip(tdls.keys(), tdls.values()):
            print("* List: " + k)

            tasks_values = list(map(utils.get_list_titles, v.values(), v.keys()))

            for task in tasks_values:
                print("  - " + task) 

    elif option == "5":
        print()

    elif option == "6":
        print()

    elif option == "7":
        print()

    elif option == "8":
        print()

    elif option == "9":
        print()

    elif option == "10":
        print()

    elif option == "11":
        print(">> Have a nice day!")
        break

    else:
        print("(!) Please select a valid option...")
