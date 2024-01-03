# OBJETOS AUXILIARES

meses = ('Janeiro','Fevereiro','Março','Abril',
           'Maio','Junho','Julho','Agosto','Setembro',
           'Outubro','Novembro','Dezembro')

meses_dias = (('Janeiro',31),('Fevereiro',29),('Março',31),
              ('Abril',30),('Maio',31),('Junho',30),('Julho',31),
              ('Agosto',31),('Setembro',30),('Outubro',31),('Novembro',30),('Dezembro',31))


# CLASSES

class Planner: 
    allTasks = []
    allDays = []

    def __init__(self, day, month):
        self.day = day
        self.month = month

    def add_task(self, task): #tarefa adicionada com a dia, mês e tarefa: Planner(18,'Novembro').add_task([titulo,descricao])
        self.allTasks.append(task)
        self.allDays.append([self.day, self.month])

    def remove_task(self, task, date):
        self.allTasks.remove(task)
        self.allDays.remove(date)
    
    def edit_task(self,oldDay, oldMonth, newDay, newMonth, oldTask, newTask):
        self.allTasks.remove(oldTask)
        self.allTasks.append(newTask)
        self.allDays.remove([oldDay, oldMonth])
        self.allDays.append([newDay, newMonth])
    
    def show_tasks(self): # imprime a lista de tarefas por ordem de adição
        if self.allTasks == []:
            print("Nenhuma tarefa encontrada")
        else:
            for i in range(len(self.allTasks)):
                print("- " + str(self.allDays[i][0]) + " de " + str(self.allDays[i][1]) + " : " + str(self.allTasks[i][0]) + ", " + str(self.allTasks[i][1]))

    def show_tasksPer_month(self, month): # recebe o mês e imprime as suas tarefas 
        allTTasks = []
        allDDays = []
        for y in self.allDays:
            if y[1] == month:
                allTTasks.append(self.allTasks[self.allDays.index(y)])
                allDDays.append(y)
        if allTTasks == []:
            print("Nenhuma tarefa no mês de " + str(month))
        else:
            for i in range(len(allTTasks)):
                print("+ " + str(allDDays[i][0]) + " : " + str(allTTasks[i][0]) + ", " + str(allTTasks[i][1]))


class Calender(): 
    year = 2024
    months = meses
    months_days = meses_dias
    
    def show_month(self, month, planner): # imprime mes (sem dias da semana) e tarefas 
        print("")
        print ("          "+month)
        print("1   2   3   4   5   6   7")
        print("8   9   10  11  12  13  14")
        print("15  16  17  18  19  20  21")
        print("22  23  24  25  26  27  28")
        i = self.months_days[self.months.index(month)][1]
        sentence = ""
        for j in range(29,i+1):
            sentence += str(j) + "  "
        print(sentence)
        print ("-------------------------------")
        planner.show_tasksPer_month(month)
        print("")


    def showAll_Months(self, plannerAll): # imprime calendário (sem dias da semana) e tarefas
        for y in self.months:
            self.show_month(y,plannerAll)
        

# FUNÇÕES AUXILIARES
def confirm_IsNumber(data): # data=(mes, dia); mes já está certo pq foi confirmado pela função abaixo. Confirma se o dia é um número e se pertence ao mês indicado antes
    if data[1].isnumeric() and (int(data[1]) in range(1, meses_dias[meses.index(data[0])][1]+1)):
        return int(data[1])
    else:
        return confirm_IsNumber((data[0],str(input("""Argumento inválido. Escreva o número correspondente ao dia do mês
>"""))))
    
def confirm_IsMonth(data): # confirma se é um mês - input tem de começar com maiúscula
    if data in meses:
        return str(data)
    else:
        return confirm_IsMonth(str(input("""Argumento inválido. Escreva o o mês (com letra inicial maiúscula); e.g. Janeiro
>""")))

# PROGRAMA

x='m'
print("Bem-vindo ao Planeador de Tarefas de 2024")
while x!='exit':

    if x=='m': #abre menu
        x = str(input("""
    MENU INICIAL
    1. Para aceder aos comandos prima 'c'
    2. Para ver a lista de tarefas prima 't'
    3. Para ver o calendário prima 'i'
    4. Para fechar o planeador escreva a palavra 'exit'
                  
>"""))

    elif x=='c': # permite ver quais os comandos que servem para manipular o planeador
        x = str(input("""
    COMANDOS
    - Para adicionar tarefa prima '+'
    - Para remover tarefa prima '-' 
    - Para editar tarefa prima 'e'
    - Para aceder ao menu prima 'm'
    
>"""))
        
    elif x=='+': # adicionar tarefa
        print("""
        ADICIONAR TAREFA""")
        mes = confirm_IsMonth(str(input("""
        - Escreva o mês (com letra inicial maiúscula); e.g. Janeiro
        >""")))
        
        dia = confirm_IsNumber((mes,str(input("""
        - Escreva o dia da tarefa a realizar; e.g. 5
        >"""))))

        titulo = str(input("""
        - Escreva o titulo da tarefa; e.g. Estudar para o teste
        >"""))
        
        descricao = str(input("""
        - Escreva uma pequena descrição da tarefa; e.g. das 15h às 13h
        >"""))
        
        Planner(dia,mes).add_task([titulo,descricao])
        x= str(input("""
        Tarefa Adicionada. Prima: 
        - 'c' para aceder aos comandos
        - 'm' para aceder ao menu
        - '+' para adicionar outra tarefa
        
>"""))

    elif x=='-': #remover tarefas
        print("""
        REMOVER TAREFA""")
        print("""
LISTA DE TAREFAS
              """)
        print ("- DIA de MÊS: TÍTULO, DESCRIÇÃO")
        print ("-------------------------------")
        Planner(0,0).show_tasks()

        choice=str(input("""
        Deseja remover alguma tarefa?
        - Se sim prima 's'
        - Caso contrário prima 'n'
        
>"""))
        
        if choice == 's': # choice serve para após o utilizador ver a lista de tarefas escolher se quer realmente remover alguma delas
            mes = confirm_IsMonth(str(input("""
        - Escreva o MÊS (com letra inicial maiúscula) da tarefa a remover; e.g. Janeiro
        >""")))

            dia = confirm_IsNumber((mes,str(input("""
        - Escreva o DIA da tarefa a remover; e.g. 5
        >"""))))

            titulo = str(input("""
        - Escreva o TÍTULO dado à tarefa
        >"""))
        
            descricao = str(input("""
        - Escreva a DESCRIÇÃO dada à tarefa
        >"""))

            if [titulo,descricao] in Planner(0,0).allTasks and [dia,mes] in Planner(0,0).allDays: # confirma se os dados fornecidos pelo utilizador estão presentes no planeador
                Planner(0,0).remove_task([titulo,descricao],[dia,mes]) # se sim, a tarefa é removida 
                x=str(input("""
        Tarefa Removida. Prima: 
        - 'c' para aceder aos comandos
        - 'm' para aceder ao menu
        - '-' para remover outra tarefa
       
>"""))
            else: # caso contrário não é removida e o utilizador pode escolher uma nova ação
                x=str(input("""
        Ocorreu um erro. A tarefa não foi removida porque não consta no planeador de tarefas.
        Tente novamente (prima '-') ou retorne ao menu incial (prima 'm')
        
>"""))
        else: # caso o input da choice for diferente de "s" então o utilizador pode escolher uma nova ação
            x=str(input("""
        Não será removida qualquer tarefa. Prima:
        - '-' para tentar novamente
        - 'c' para aceder aos comandos
        - 'm' para aceder ao menu
        
>"""))
            
    elif x=='e': # editar tarefa
        print("""
        EDITAR TAREFA
              """)
        print("""
LISTA DE TAREFAS:
              """)
        print ("- DIA de MÊS: TÍTULO, DESCRIÇÃO")
        print ("-------------------------------")
        Planner(0,0).show_tasks()

        choice=str(input("""
        Deseja editar alguma tarefa?
        - Se sim prima 's'
        - Caso contrário prima 'n'
        
>"""))
           
        if choice == 's': # choice serve para após o utilizador ver a lista de tarefas escolher se quer realmente editar alguma delas

            mes = confirm_IsMonth(str(input("""
        - Escreva o MÊS (com letra inicial maiúscula) da tarefa a editar; e.g. Janeiro
        >""")))

            dia = confirm_IsNumber((mes,str(input("""
        - Escreva o DIA da tarefa a editar; e.g. 5
        >"""))))

            titulo = str(input("""
        - Escreva o TÍTULO dado à tarefa
        >"""))
        
            descricao = str(input("""
        - Escreva a DESCRIÇÃO dada à tarefa
        >"""))

            if [titulo,descricao] in Planner(0,0).allTasks and [dia,mes] in Planner(0,0).allDays: # confirma se os dados fornecidos pelo utilizador estão presentes no planeador
                # se sim, pode-se começar a editar a tarefa
                # escolhendo o que se quer editar
                choice=str(input("""
        Deseja editar:
        1) a data da tarefa - prima '1'
        2) o título e descrição da tarefa - prima '2'
        3) ambos - prima '3'
        
>"""))
                
                if choice == '1': #editar data

                    novoMes = confirm_IsMonth(str(input("""
        - Escreva o NOVO MÊS (com letra inicial maiúscula) pretendido; e.g. Abril
        >""")))

                    novoDia = confirm_IsNumber((novoMes,str(input("""
        - Escreva o NOVO DIA pretendido; e.g. 20
        >"""))))
                    Planner(0,0).edit_task(dia, mes, novoDia, novoMes, [titulo,descricao], [titulo,descricao])

                    x=str(input("""
        Tarefa Editada. Prima: 
        - 'c' para aceder aos comandos
        - 'm' para aceder ao menu
        - 'e' para editar outra tarefa
        
>"""))
                    

                elif choice == '2': #editar título/descrição

                    novoTitulo = str(input("""
        - Escreva o NOVO TÍTULO pretendido
        >"""))
            
                    novoDescricao = str(input("""
        - Escreva a NOVA DESCRIÇÃO pretendida
        >"""))
                    Planner(0,0).edit_task(dia, mes, dia, mes, [titulo,descricao], [novoTitulo, novoDescricao])

                    x=str(input("""
        Tarefa Editada. Prima: 
        - 'c' para aceder aos comandos
        - 'm' para aceder ao menu
        - 'e' para editar outra tarefa
        
>"""))

                elif choice == '3': #editar ambos

                    novoMes = confirm_IsMonth(str(input("""
        - Escreva o NOVO MÊS (com letra inicial maiúscula) pretendido; e.g. Abril
        >""")))

                    novoDia = confirm_IsNumber((novoMes,str(input("""
        - Escreva o NOVO DIA pretendido; e.g. 20
        >"""))))
                    
                    novoTitulo = str(input("""
        - Escreva o NOVO TÍTULO pretendido
        >"""))
            
                    novoDescricao = str(input("""
        - Escreva a NOVA DESCRIÇÃO pretendida
        >"""))
                    Planner(0,0).edit_task(dia, mes, novoDia, novoMes, [titulo,descricao], [novoTitulo, novoDescricao])
                    
                    x=str(input("""
        Tarefa Editada. Prima: 
        - 'c' para aceder aos comandos
        - 'm' para aceder ao menu
        - 'e' para editar outra tarefa
        
>"""))

                else: # caso input do choice for diferente de 1, 2 ou 3 então utilizador pode escolher nova ação
                    x=str(input("""
        Opção escolhida não consta na lista de opções. Prima: 
        - 'c' para aceder aos comandos
        - 'm' para aceder ao menu
        - 'e' para tentar novamente
        
>"""))
                    
            else: # caso a tarefa escolhida não esteja na lista de tarefas
                x=str(input("""
        Ocorreu um erro. A tarefa não foi editada porque não consta no planeador de tarefas.
        Tente novamente (prima 'e') ou retorne ao menu incial (prima 'm')

>"""))
        else: # caso o utilizador não queira editar qq tarefa da lista
            x=str(input("""
        Não será editada qualquer tarefa. Prima:
        - 'e' para tentar novamente
        - 'c' para aceder aos comandos
        - 'm' para aceder ao menu
                    
>"""))
    
    elif x=="t": # imprime a lista de tarefas
        print("""
LISTA DE TAREFAS:
              """)
        Planner(0,0).show_tasks()

        x="m"

    elif x=='i': # acesso ao calendário (1 - mostra o mês; 2- mostra todos os meses)
        print("""
        CALENDÁRIO
              """)
        choice=str(input("""
        Deseja aceder ao:
        1) calendário simplificado do ano de 2024, prima '1'
        2) calendário simplificado de um mês específico, prima '2'
                             
>"""))
        if choice == '1':

            Calender().showAll_Months(Planner(0,0))
        
        elif choice == '2':

            mes = confirm_IsMonth(input("""
        - Escreva o MÊS (com letra inicial maiúscula) pretendido; e.g. Abril
        >"""))
    
            Calender().show_month(mes, Planner(0,0))

        else: # caso choice seja diferente de 1 ou de 2 então o utilizador é informado
                    print("""
        Opção escolhida não consta na lista de opções.
        """)
        # o utilizador volta ao menu
        x="m"
         
    else: # caso a opção escolhida seja diferente das do menu e comandos então utilizador vota para o menu
        print("""
    Opção escolhida não consta na lista de opções. Vamos regressar para o menu
             """)
        x='m'

