# HACKERSCHOOL

# PYTHON PROJECT 2023/2024 RECRUITMENT

The application can be executed, while in the directory, by:

```python3 main.py```

This simple application was done as a project for new recruits to HackerSchool. It is a Task List,
that allows one to add, list, remove and edit tasks. Each task has a name (title), description, and 
an attribute that verifies if they are done.

The application interacts with the user through a simple Command Line Interface (CLI), that builds
two menus, main menu and edit menu, through which commands are chosen in accord with its "code"
(each command has a "code", which is an integer)

There are three main files:

- ```main.py``` - File with the various menus, and functions to interact with the user, using methods of the TaskList class during the process  
     
- ```task_list.py``` - File with the class TaskList, that stores and manges the  various tasks, being used by functions in main.py and using methods in task.py  
     
- ```task.py``` - File with the class Task, not used directly by main.py, but used by TaskList class methods in task_list.py 

The application, while running, allows the user to interact with the Task List Apllication by:

- List all Tasks: 
    This command writes all Tasks curently registered in the program, along with its ID, name(title), description, along with its status ("Done" or "Not Done")

- Add a Task:
    This command allows the user to add a new task, asking the user for its name and description. The application automatically puts the status of the Task as "Not Done" and the ID as next integer 
    after the ID of the last Task in list (e.g. if the last Task has ID=56, new Task will have ID=57) 

- Edit a Task:
    This command, opens a new menu in terminal, with several options of edit:
  
    - Edit Name - After selecting this command, and the task (through the ID) to be edited, it will ask the user for the new task name.
   
    - Edit Description - After selecting this command, and the task (through the ID) to be edited, it will ask the user for the new task description.
  
    - Mark as done - After selecting this command, and the task (through the ID) to be edited, it will mark the task as done.
  
    - Exit - When the editing is done, returns to the main menu.
    
    In this menu, the inputs of the user (task ID and command) are verified to be correct, if not, they 
    are asked for again, repeatedly.

- Remove a Task:
    This command allows the user to remove one of the existing Tasks, by asking for a valid Task ID, 
    and double checking with the user. In the double check, if the user inputs a invalid input, "n" or "N" ,
    the task will not be deleted, and will be deleted if the answer is "y" or "Y".

- Exit: 
    This command allows the user to close the application.