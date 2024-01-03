class TaskList:
    _tasks = None #List of tasks

    def __init__(self):
        #Initialize the list
        self._tasks = []

    def add_task(self, task): 
        #Add a task to the list
        self._tasks.append(task)
    
    def remove_task(self, id): #Remove a task from the list
        task = self._tasks[int(id)-1] #Get the task with the given id
        self._tasks.remove(task) #Remove the task from the list
        size = len(self._tasks) #Current size of the list
        for i in range(task.get_id()-1, size):
            #Update the id of the tasks after the removed one
            self._tasks[i].set_id(i+1)

    def get_task(self, id): #Get a task from the list
        if int(id) < 0 or int(id) > len(self._tasks):
            #Invalid id
            return None
        #Return the task with the given id
        return self._tasks[int(id)-1]

    def get_all_tasks(self): 
        #Get all tasks from the list
        return self._tasks

    def get_number_of_tasks(self): 
        #Get the number of tasks in the list
        return len(self._tasks)

    def edit_task_description(self, id, description): 
        #Edit the description of a task
        # id - 1 because the list starts from 0 and task ids start from 1 
        self._tasks[int(id)-1].set_description(description)
    
    def edit_task_name(self, id, name): 
        #Edit the name of a task
        # id - 1 because the list starts from 0 and task ids start from 1 
        self._tasks[int(id)-1].set_name(name)
    
    def finish_task(self, id): 
        #Finish a task
        # id - 1 because the list starts from 0 and task ids start from 1 
        self._tasks[int(id)-1].finish()

    def print_all_tasks(self):
        #Print all tasks from the list
        for task in self._tasks:
            print(task)