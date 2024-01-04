import os
from classListaTarefas import ListaTarefas
             

# Função importada com o intuito de limpar o terminal durantes as transições
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
