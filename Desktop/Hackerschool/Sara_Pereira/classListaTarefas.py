import os


# Classe com as várias opções de alterar a lista de tarefas                                                                          
class ListaTarefas:                                                     
    def __init__(self):
        self.elementos = []

    # Função que adiciona tarefas à lista
    def acrescentar(self, elemento, descricao=""):                                    
        self.elementos.append(f"{elemento}||{descricao}")
        print(f'A tarefa "{elemento}" foi adicionada com sucesso.')
  

    def remover(self, iTarefa):
        if 1 <= iTarefa <= len(self.elementos):
            self.elementos.pop(iTarefa - 1)
            print(f'A tarefa foi removida.')
        else:
            print(f'A tarefa de indíce {iTarefa} não foi encontrada.')

    # Função que permite consultar a lista atual 
    def ver(self):              
        # Caso vazia                                                             
        if not self.elementos:
            print('Não tens nada para fazer.') 
        # Caso com pelo menos um elemento                                                             
        else:
            print('Lista de Tarefas:')                                  
            for i, elemento in enumerate(self.elementos, start=1):
                tarefa, descricao = elemento.split('||')
                print(f'{i}. {tarefa}')
                print(f'Descrição: {descricao}')
                print()

    # Função que edita a lista
    def editar(self,iTarefa):
        # Se iTarefa (indice da tarefa) estiver no intervalo, a tarefa é editada
        if iTarefa <= len(self.elementos):                                                  
            nova_tarefa = input(f"Editar a tarefa {self.elementos[iTarefa-1].split('||')[0]} para: ")
            nova_descricao = input(f"Editar a descrição {self.elementos[iTarefa-1].split('||')[1]} para: ")
            self.elementos[iTarefa-1] = (f"{nova_tarefa}||{nova_descricao}")
            print(f'Tarefa editada com sucesso.')
        # Caso contrario nada sofre alterações
        else:
            print('Não foi possível editar.')

    # Função que exporta a lista
    def exportar(self):
        # A lista é guardada na mesma pasta com o nome 'lista_tarefas.txt'
        with open('lista_tarefas.txt', 'w') as arquivo:
            for i, elemento in enumerate(self.elementos, start=1):
                tarefa, descricao = elemento.split('||')
                arquivo.write(f'{i}.{tarefa}\n')
                arquivo.write(f'Descrição: {descricao}')
                print(f'Lista exportada para com sucesso.')                   

# Função importada com o intuito de limpa o terminal durantes as transições
def clear_screen():
    # Limpa o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

# Mostra as opções do menu
def opcoes():
    print("Lista de Tarefas")
    print()
    print("(1) Acrescentar")
    print("(2) Remover")
    print("(3) Ver lista")
    print("(4) Editar lista")
    print("(5) Exportar lista")    
    print("(6) Sair")
    print()

# Função main
def main():
    lista = ListaTarefas()
    escolha = None


    while escolha is None:
        # Apaga tudo o que estava antes, mostra o menu e consoante o input realiza as seguintes tarefas:
        clear_screen()
        opcoes()
        escolha = input("Escolha uma opção: ")
        
        # Se o input for 1, adiciona tarefas à lista
        if escolha == '1':
            clear_screen()
            tarefa = input('Escreve o que queres acrescentar: ')
            descricao = input('Escreve uma descrição para a tarefa: ')
            lista.acrescentar(tarefa, descricao)
            escolha = None
            input()
        
        # Se o input for 2, remove tarefas à lista (se de facto existirem tarefas)
        elif escolha == '2':
            clear_screen()
            lista.ver()
            print()
            print("Para voltar ao menu clica qualquer outra tecla fora os indices da tua lista")
            print()
            try:
                iTarefa = int(input("Qual é o número da tarefa que queres apagar? "))
                if 1 <= iTarefa:
                    lista.remover(iTarefa)
                    escolha = None
                    input()
                else:
                    escolha = None 

            except ValueError:
                print("Por favor escolhe um número que corresponda ao índice da tua lista")
                escolha = None
                clear_screen()

        # Se o input for 3, abre a lista
        elif escolha == '3':
            clear_screen()
            lista.ver()
            print()
            print("Clica em qualquer tecla para voltar ao menu")
            escolha = None
            input()

        # Se o input for 4, dá a opção de editar uma tarefa existente
        elif escolha == '4':
            clear_screen()  
            lista.ver()
            print()
            print("Para voltar ao menu clica qualquer outra tecla fora os indices da tua lista")
            print() 
            try:
                iTarefa = int(input("Qual é o número da tarefa que queres editar? "))
                if 1 <= iTarefa:
                    lista.editar(iTarefa)
                    escolha = None
                    input()
                else:
                    escolha = None 

            except ValueError:
                print("Por favor escolhe um número que corresponda ao indíce da tua lista")
                escolha = None
                clear_screen()  

        # Se o input for 5, exporta a lista para a pasta onde está o programa
        elif escolha== '5':
            clear_screen()
            lista.exportar()
            escolha = None
            input()

        # Se o input for 6, limpa o terminal fecha o programa
        elif escolha == '6':
            clear_screen()
            break

        # Se o input for qualquer outro, pede um input valido e redireciona ao menu
        else:
            escolha = None
            clear_screen()
            print("Por favor escolhe um número inteiro entre 1 e 4")
            input()

# Corre o programa
if __name__ == "__main__":
    main()
