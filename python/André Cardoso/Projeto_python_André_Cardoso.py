import os


class task_manager():

    #classe que cria e gere a lista de tasks

    def __init__(self):

        #lista (dictionary) em que as keys são os nomes das tasks e os values as respectivas descriçoes

        self.tasks = {}

        #usado para descobrir o path até ao folder onde ta o programa

        program_path = os.path.abspath(__file__)
        self.program_folder = os.path.dirname(program_path)

        #função que acessa um txt e tira de la nomes e descrições de tasks guardadas

        self.get_tasks_from_txt()

    def get_tasks_from_txt(self):

        #função que acessa um txt e tira de la nomes e descrições de tasks guardadas

        with open(self.program_folder + "\\tasks.txt", "r") as file:

            tasks_txt = file.read()
            name_and_desc = tasks_txt.split("\n")

            for i in range(0, len(name_and_desc) - 1, 2):

                self.add_task(name_and_desc[i], name_and_desc[i + 1])   


    def add_task(self, name, desc):

        #função que cria e adiciona uma task á lista de tasks

        self.tasks[name] = desc

    def remove_task(self, name):
        
        #função que remove uma task da lista

        del self.tasks[name]

            
    def change_name(self, name, new_name):

        #função que muda o nome de uma task, mantendo a sua descrição

        value = self.tasks.get(name)

        self.remove_task(name)
        self.add_task(new_name, value)

    def change_desc(self, name, new_desc):

        #função que muda a descrição de uma task, mantendo o seu nome 

        self.tasks[name] = new_desc

    def print_task_list(self) : 

        #função que da print nas tasks atuais, e se não houver tasks diz que não existem tasks

        for task in self.tasks:
            
            print(f"\nname:{task} ---> description:{self.tasks[task]}")

        if len(self.tasks) == 0:

            print("You don't have any tasks")

    def save_tasks_in_txt(self):

        #função que grava as tasks atuais num ficheiro txt chamado "tasks.txt" localizado na mesma pasta que o programa

        name_list = list(self.tasks.keys())

        with open(self.program_folder + "\\tasks.txt", "w") as file:
            
            for i in range(0, len(self.tasks)):

                name = name_list[i]

                file.write(f"{name}\n{self.tasks[name]}\n")


task_manager = task_manager()

while True:

    #ciclo while para o programa estar sempre a ser executado

    choice = input("\nWhat do you want to do? Type:\n1 - See task list\
                   \n2 - Add a task to the list\
                   \n3 - Remove a task from the list\
                   \n4 - Change a task name\
                   \n5 - Change a descripion of a task\
                   \n6 - End the Task Manager\
                   \n(type exit at any moment to return to this menu)\n")
    
    if choice == str(1):

        #print a task list

        task_manager.print_task_list()

    elif choice == str(2):

        #pede um nome e descrição de task e adiciona á lista

        while True:

            name = input("\nSelect the name of the task:\n")

            if name == "exit":

                break

            elif name in task_manager.tasks:

                print(f"You already have a task named that, choose another name\n\
here are the name and descriptions of your current tasks:\n")
                task_manager.print_task_list()

            else: 

                break

        if name != "exit":

            desc = input("Select the task description:\n")

            if desc != "exit":

                task_manager.add_task(name, desc)

    elif choice == str(3):

        #pede um nome de uma task existente para remover da lista

        while True:

            print(f"\nHere are the name and descriptions of your current tasks\n")
            task_manager.print_task_list()
            name = input("\nplease say the name of the task you want to remove:\n")

            if name == "exit":

                break
            
            elif name not in task_manager.tasks:

                print("Please select a task in your current task list")

            else: 

                task_manager.remove_task(name)
                break

    elif choice == str(4):
         
        #pede o nome de uma task existente para mudar o nome dessa task para outro nome á escolha

         while True:

            print(f"\nHere are the name and descriptions of your current tasks\n")
            task_manager.print_task_list()
            name = input("\nplease say the name of the task you want to change the name:\n")

            if name == "exit": 

                break
            
            elif name not in task_manager.tasks:

                print("Please select a task in your current task list")

            else: 

                while True:

                    new_name = input("Now select the new name you want on the task:\n")

                    if new_name == "exit":

                        break

                    elif new_name in task_manager.tasks:

                        print(f"Select a valid name, that name is already in your tasks list\
                        here are here are the name and descriptions of your current tasks:\n")
                        task_manager.print_task_list()

                    else:

                        task_manager.change_name(name, new_name)
                        break

                break



    elif choice == str(5):

        #pede o nome de uma task existente para mudar a descrição dessa task para outra descrição á escolha

        while True:

            print(f"\nHere are the name and descriptions of your current tasks\n")
            task_manager.print_task_list()
            name = input("\nplease say the name of the task you want to change the description:\n")

            if name == "exit":

                break

            elif name not in task_manager.tasks:

                print("Please select a task in your current task list")

            else: 

                new_desc = input("Now Select the new description you want that task to have:\n")

                if new_desc != "exit":

                    task_manager.change_desc(name, new_desc)

                break

    elif choice == str(6):

        #acaba o ciclo while, acabando assim o programa

        break

    elif choice == str(7):

        #By Rick Astley

        print("\n\
        Never gonna give you up\n\
        Never gonna let you down\n\
        Never gonna turn around and desert you\n\
        Never gonna make you cry\n\
        Never gonna say goodbye\n\
        Never gonna tell a lie and hurt you\n")

    else:

        #caso o input não seja um numero de 1 a 7

        print("Please select a valid option")



#fim do programa, e refaz o txt para condizer com as task atuais da lista de tasks
        
task_manager.save_tasks_in_txt()



    













            


        


        
        

    