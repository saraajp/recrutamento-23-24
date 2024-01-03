# Inicial task list and description dictionary
tasks = []
descriptions = {}

# Auxiliary functions
def displayTasks(tasks, descriptions):
    '''
    This function displays the list of all tasks added and their descriptions
    on the screen.
    '''

    print('\nYour tasks: ')
    if len(tasks) == 0:
        print('No tasks!\n')
    else:
        for index, task in enumerate(tasks):
            print(f'{index+1}: {task} - {descriptions[task]}')
        print('\n')

def newOperation(all_tasks, descriptions):
    '''
    This function asks the user which operation is going to be performed:
    "A": Add task;
    "R": Remove task;
    "E": Edit task;
    "F": Quit the application.
    '''

    operation = input('Press "A" to add a new task, "R" to remove a task, "E" to edit a task or "F" to exit: ')
    if operation == 'A':
        addTask(all_tasks, descriptions)
    elif operation == 'R':
        removeTask(all_tasks, descriptions)
    elif operation == 'E':
        editTask(all_tasks, descriptions)
    elif operation == 'F':
        displayTasks(all_tasks, descriptions)
        return
    else:
        newOperation(all_tasks, descriptions)

# Operations
def addDescription(task, descriptions):
    '''
    This function allows the user to provide a task description when adding a
    new task.
    '''

    description = input('Add task decription: ')

    descriptions[task] = description
    return descriptions

def removeTask(all_tasks, descriptions):
    '''
    This function receives a list with all the added tasks and respective
    descriptions and removes one of them, returning the updated task list
    and descriptions dictionary.
    '''

    task_number = input('Enter the number of the task you want to remove: ')

    while not (0 < int(task_number) <= len(all_tasks)):
        task_number = input('Please provide a valid task number: ')

    del descriptions[all_tasks[int(task_number)-1]]
    all_tasks.remove(all_tasks[int(task_number)-1])

    print(f'\nItem {task_number} removed!')
    displayTasks(all_tasks, descriptions)

    newOperation(all_tasks, descriptions)

def editTask(all_tasks, descriptions):
    '''
    This function receives a list with all the added tasks and respective 
    descriptions and allows the user to edit one of them, returning the 
    updated task list and descriptions dictionary.
    '''

    task_number = input('Enter the number of the task you want to edit: ')

    while not (0 < int(task_number) <= len(all_tasks)):
        task_number = input('Please provide a valid task number: ')

    new_task = input('Edit task: ')
    all_tasks[int(task_number)-1] = new_task
    new_description = input('Edit description: ')
    descriptions[new_task] = new_description

    print(f'\nItem {task_number} edited!')
    displayTasks(all_tasks, descriptions)

    newOperation(all_tasks, descriptions)

def addTask(all_tasks, descriptions):
    '''
    This function receives a list with all the added tasks and allows the user
    to add another one, returning the updated task list.
    '''

    task = input('Add a task: ')
    all_tasks.append(task)
    new_descriptions = addDescription(task, descriptions)
    displayTasks(tasks, new_descriptions)

    newOperation(tasks, new_descriptions)

# Start application
addTask(tasks, descriptions)