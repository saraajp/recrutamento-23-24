class Task:
    _id = None #Task id
    _name = None #Task name/title
    _description = None #Task description
    done = None #Task status

    def __init__(self, id,  name, description):
        #Initialize the task
        self._id = id
        self._name = name
        self._description = description 
        self.done = "Not done"

    def finish(self): 
        #Identify a task as done
        self.done = "Done"
    
    def get_id(self): 
        #Get the task id
        return self._id

    def set_id(self, id): 
        #Set the task id
        self._id = id
    
    def get_name(self): 
        #Get the task name
        return self._name
    
    def set_name(self, name): 
        #Set the task name, in case of an edit
        self._name = name

    def get_description(self): 
        #Get the task description
        return self._description
    
    def set_description(self, description): 
        #Set the task description, in case of an edit
        self._description = description 

    def __str__(self):
        #Print the task
        return f"Task {self._id}: Name: {self._name} - Description: {self._description} - {self.done}"