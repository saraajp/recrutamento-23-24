import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QCalendarWidget, QLabel, QPushButton, QLineEdit, QMessageBox, QListWidget, QTimeEdit
from PyQt5.QtCore import QDate,QTime

class TaskManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("O gestor")  # Define o título da janela
        self.setGeometry(400, 400, 400, 600)  # Define a geometria da janela

        self.calendar = QCalendarWidget(self)  # Cria um widget de calendário
        self.calendar.setMinimumDate(QDate.currentDate())  # Define a data mínima selecionável como a data atual
        self.calendar.selectionChanged.connect(self.on_date_selected)  # Conecta o sinal de seleção de data ao método on_date_selected

        self.task_label = QLabel("Adicionar Tarefa:", self)  # Cria um rótulo para a seção de adicionar tarefa
        self.task_name_label = QLabel("Nome:", self)  # Cria um rótulo para o campo de nome da tarefa
        self.task_name_input = QLineEdit(self)  # Cria um campo de entrada para o nome da tarefa
        self.task_desc_label = QLabel("Descrição:", self)  # Cria um rótulo para o campo de descrição da tarefa
        self.task_desc_input = QLineEdit(self)  # Cria um campo de entrada para a descrição da tarefa
        self.task_time_label = QLabel("Hora:", self)  # Cria um rótulo para o campo de hora da tarefa
        self.task_time_input = QTimeEdit(self)  # Cria um campo de entrada para a hora da tarefa usando QTimeEdit
        self.add_button = QPushButton("Adicionar Tarefa", self)  # Cria um botão para adicionar tarefa
        self.add_button.clicked.connect(self.add_task)  # Conecta o sinal de clique do botão ao método add_task

        self.remove_button = QPushButton("Remover Tarefa", self)  # Cria um botão para remover tarefa
        self.remove_button.clicked.connect(self.remove_selected_task)  # Conecta o sinal de clique do botão ao método remove_selected_task

        self.layout = QVBoxLayout()  # Cria um layout vertical
        self.layout.addWidget(self.calendar)  # Adiciona o widget de calendário ao layout
        self.layout.addWidget(self.task_label)  # Adiciona o rótulo da seção de adicionar tarefa ao layout
        self.layout.addWidget(self.task_name_label)  # Adiciona o rótulo do campo de nome da tarefa ao layout
        self.layout.addWidget(self.task_name_input)  # Adiciona o campo de entrada do nome da tarefa ao layout
        self.layout.addWidget(self.task_desc_label)  # Adiciona o rótulo do campo de descrição da tarefa ao layout
        self.layout.addWidget(self.task_desc_input)  # Adiciona o campo de entrada da descrição da tarefa ao layout
        self.layout.addWidget(self.task_time_label)  # Adiciona o rótulo do campo de hora da tarefa ao layout
        self.layout.addWidget(self.task_time_input)  # Adiciona o campo de entrada da hora da tarefa ao layout
        self.layout.addWidget(self.add_button)  # Adiciona o botão de adicionar tarefa ao layout
        self.layout.addWidget(self.remove_button)  # Adiciona o botão de remover tarefa ao layout

        self.central_widget = QWidget(self)  # Cria um widget central
        self.central_widget.setLayout(self.layout)  # Define o layout do widget central
        self.setCentralWidget(self.central_widget)  # Define o widget central como o widget central da janela

        self.tasks = []  # Lista para armazenar as tarefas

        self.task_viewer = QListWidget(self)  # Cria um widget de lista para exibir as tarefas
        self.task_viewer.setGeometry(100, 500, 500, 500)  # Aumenta a altura do widget de lista
        self.layout.addWidget(self.task_viewer)  # Adiciona o widget de lista ao layout
        self.task_viewer.itemDoubleClicked.connect(self.edit_task)  # Conecta o sinal de clique duplo do item ao método edit_task

    def on_date_selected(self):
        selected_date = self.calendar.selectedDate()  # Obtém a data selecionada no calendário
        sorted_tasks = sorted(self.tasks, key=lambda task: task['date'])  # Ordena as tarefas com base na proximidade com a data selecionada
        self.display_tasks(sorted_tasks)  # Exibe as tarefas ordenadas

    def add_task(self):
        task_name = self.task_name_input.text()  # Obtém o nome da tarefa do campo de entrada
        task_desc = self.task_desc_input.text()  # Obtém a descrição da tarefa do campo de entrada
        task_time = self.task_time_input.time().toString("hh:mm")  # Obtém a hora da tarefa do campo de entrada
        selected_date = self.calendar.selectedDate()  # Obtém a data selecionada no calendário
        if selected_date < QDate.currentDate():  # Verifica se a data selecionada é anterior à data atual
            QMessageBox.warning(self, "Data Inválida", "Não é possível adicionar tarefas no passado.")  # Exibe uma mensagem de aviso
        else:
            self.tasks.append({'date': selected_date, 'name': task_name, 'description': task_desc, 'time': task_time})  # Adiciona a tarefa à lista de tarefas
            self.task_name_input.clear()  # Limpa o campo de entrada do nome da tarefa
            self.task_desc_input.clear()  # Limpa o campo de entrada da descrição da tarefa
            self.task_time_input.clear()  # Limpa o campo de entrada da hora da tarefa
            self.display_tasks(self.tasks)  # Exibe as tarefas atualizadas

    def remove_selected_task(self):
        selected_items = self.task_viewer.selectedItems()  # Obtém os itens selecionados na lista de tarefas
        if not selected_items:
            QMessageBox.warning(self, "Nenhuma Tarefa Selecionada", "Selecione uma tarefa para remover.")  # Exibe uma mensagem de aviso se nenhum item estiver selecionado
        else:
            for item in selected_items:
                index = self.task_viewer.row(item)  # Obtém o índice do item selecionado
                self.tasks.pop(index)  # Remove a tarefa da lista de tarefas
            self.display_tasks(self.tasks)  # Exibe as tarefas atualizadas

    def edit_task(self, item):
        index = self.task_viewer.row(item)  # Obtém o índice do item selecionado
        task = self.tasks[index]  # Obtém a tarefa correspondente ao índice
        task_name = task['name']
        task_desc = task['description']
        task_time = task['time']
        self.task_name_input.setText(task_name)  # Preenche o campo de entrada do nome da tarefa com o nome da tarefa selecionada
        self.task_desc_input.setText(task_desc)  # Preenche o campo de entrada da descrição da tarefa com a descrição da tarefa selecionada
        self.task_time_input.setTime(QTime.fromString(task_time, "hh:mm"))  # Preenche o campo de entrada da hora da tarefa com a hora da tarefa selecionada

        # Remove the task from the list
        self.tasks.pop(index)
        self.display_tasks(self.tasks)  # Exibe as tarefas atualizadas

    def display_tasks(self, tasks):
        self.task_viewer.clear()  # Limpa o widget de lista de tarefas
        for task in tasks:
            task_item = f"Data: {task['date'].toString('yyyy-MM-dd')}, Nome: {task['name']}, Descrição: {task['description']}, Hora: {task['time']}"  # Formata a string da tarefa
            self.task_viewer.addItem(task_item)  # Adiciona a tarefa ao widget de lista

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Fechar Janela', 'Tem certeza que deseja fechar a janela?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            confirm_reply = QMessageBox.question(self, 'Fechar Janela', 'Tens mm a certeza?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if confirm_reply == QMessageBox.Yes:
                replyaserio= QMessageBox.question(self, 'Fechar Janela', 'Fr?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if replyaserio == QMessageBox.Yes:
                    event.accept()
                else:
                    event.ignore()
            else:
                event.ignore()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Cria uma instância da aplicação
    task_manager = TaskManagerApp()  # Cria uma instância da classe TaskManagerApp
    task_manager.show()  # Exibe a janela
    sys.exit(app.exec_())  # Executa o loop de eventos da aplicação
