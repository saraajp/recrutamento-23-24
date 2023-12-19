import os
from task import Task
from task_list import TaskList

def list_all_tasks(task_list): 
    #List all tasks from the list
    print("Listing all tasks:")
    task_list.print_all_tasks() #Print all tasks
    input("Press enter to continue: ") #Wait for user input
    os.system('clear') #Clear the screen

def add_task(task_list): 
    #Add a task to the list
    print("Adding a new task:")
    name = input("Enter the task name: ") #Get the task name
    description = input("Enter the task description: ") #Get the task description
    #Add the task to the list, with the id being the number of tasks + 1
    task_list.add_task(Task(task_list.get_number_of_tasks()+1, name, description))

    #Print the task that was added
    print(task_list.get_task(task_list.get_number_of_tasks()))
    print("Task added successfully!")
    input("Press enter to continue: ") #Wait for user input
    os.system('clear') #Clear the screen

def editing_menu(task_list): 
    #Print the editing menu
    while True: #Editing loop
        print("Editing a task:")
        
        print("Please select one of the following options:")
        #Print the editing menu
        print("1. Edit the name")
        print("2. Edit the description")
        print("3. Mark as done")
        print("0. Exit")

        choice = input("Enter the number of your choice: ") #Get the user choice
        os.system('clear') #Clear the screen
        if choice.isnumeric() == False or int(choice) < 0 or int(choice) > 3:
            #Invalid choice
            print("Invalid choice. Please enter a valid option.")
            continue
        
        if choice == "0":
            #Exit the editing menu
            print("Exiting editing menu!")
            break
        
        #Get a valid task id
        while True:
            id = input("Enter the task id: ")
            #Check if the id is valid
            if id.isnumeric()==False or task_list.get_task(id) == None:
                print("Invalid id. Please enter a valid id.")
            else:
                break
        
        match choice:
            case "1":
                #Edit the name of the task
                task_list.edit_task_name(id, input("Enter the new name: "))
                print("Task name edited successfully!")
            case "2":
                #Edit the description of the task
                task_list.edit_task_description(id, input("Enter the new description: "))
                print("Task description edited successfully!")
            case "3":
                #Mark the task as done
                task_list.finish_task(id)
                print("Task marked as done.")

def delete_task(task_list): #Delete a task from the list
    print("Deleting a task:")
    while True: #Get a valid task id
        id = input("Enter the task id: ")
        if id.isnumeric() == False: #Check if the id is numerical
            print("Invalid id. Please enter a valid id.")
        
        task = task_list.get_task(id)
        if task == None: #Check if the task exists
            print("Invalid id. Please enter a valid id.")
        else:
            break
    print(task) #Print the task
    #Ask for confirmation
    confirmation = input("Are you sure you want to delete this task? (Y/N)")

    #Check the confirmation
    if (confirmation == "Y" or confirmation == "y"):
        #Delete the task
        task_list.remove_task(id)
        print("Task deleted successfully!")
    elif (confirmation == "N" or confirmation == "n"):
        #Don't delete the task
        print("Task not deleted.")
    else:
        #Invalid choice
        print("Invalid choice. Task not deleted.")

    input("Press enter to continue: ") #Wait for user input
    os.system('clear') #Clear the screen

def main():
    #Create a new task list
    task_list = TaskList()
    print("Welcome to the Task Manager!")
    while True: #Main loop
        #Print the Main Menu
        print("Please select one of the following options:")
        print("1. List all Tasks")
        print("2. Add a Task")
        print("3. Edit a Task")
        print("4. Delete a Task")
        print("0. Exit")

        choice = input("Enter the number of your choice: ") #Get the user choice
        os.system('clear') #Clear the screen

        if choice.isnumeric() == False or int(choice) < 0 or int(choice) > 4:
            print("Invalid choice. Please enter a valid option.")
            continue
        
        match choice:
            case "0": 
                #Exit the program
                print("Exiting the program. Goodbye!")
                break
            case "1": #List all tasks
                if task_list.get_number_of_tasks() == 0:
                    #There are no tasks to list
                    print("There are no tasks to list.")
                else:
                    #List all tasks
                    list_all_tasks(task_list)
            case "2":
                #Add a task
                add_task(task_list)
            case "3":
                #Edit a task
                if task_list.get_number_of_tasks() == 0:
                    #There are no tasks to edit
                    print("There are no tasks to edit.")
                else:
                    #Edit a task
                    editing_menu(task_list)
            case "4":
                #Delete a task
                if task_list.get_number_of_tasks() == 0:
                    #There are no tasks to delete
                    print("There are no tasks to delete.")
                else:
                    #Delete a task
                    delete_task(task_list)

if __name__ == "__main__":
   main()
