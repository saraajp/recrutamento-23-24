import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QCalendarWidget, QLabel, QPushButton, QLineEdit, QMessageBox, QListWidget, QTimeEdit
from PyQt5.QtCore import QDate,QTime

class TaskManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("O gestor")  # Define o título da janela
        self.setGeometry(400, 400, 400, 600)  # Define a geometria da janela

        # Widget de calendário
        self.calendar = QCalendarWidget(self)
        self.calendar.setMinimumDate(QDate.currentDate())  # Define a data mínima selecionável como a data atual
        self.calendar.selectionChanged.connect(self.on_date_selected)  # Conecta o sinal de seleção de data ao método on_date_selected

        # Seção de adicionar tarefa
        self.task_label = QLabel("Adicionar Tarefa:", self)
        self.task_name_label = QLabel("Nome:", self)
        self.task_name_input = QLineEdit(self)
        self.task_desc_label = QLabel("Descrição:", self)
        self.task_desc_input = QLineEdit(self)
        self.task_time_label = QLabel("Hora:", self)
        self.task_time_input = QTimeEdit(self)
        self.add_button = QPushButton("Adicionar Tarefa", self)
        self.add_button.clicked.connect(self.add_task)

        # Botão de remover tarefa
        self.remove_button = QPushButton("Remover Tarefa", self)
        self.remove_button.clicked.connect(self.remove_selected_task)

        # Layout vertical
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.calendar)
        self.layout.addWidget(self.task_label)
        self.layout.addWidget(self.task_name_label)
        self.layout.addWidget(self.task_name_input)
        self.layout.addWidget(self.task_desc_label)
        self.layout.addWidget(self.task_desc_input)
        self.layout.addWidget(self.task_time_label)
        self.layout.addWidget(self.task_time_input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.remove_button)

        # Widget central
        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.tasks = []  # Lista para armazenar as tarefas

        # Widget de lista para exibir as tarefas
        self.task_viewer = QListWidget(self)
        self.task_viewer.setGeometry(100, 500, 500, 500)
        self.layout.addWidget(self.task_viewer)
        self.task_viewer.itemDoubleClicked.connect(self.edit_task)

    # Método chamado quando uma data é selecionada no calendário
    def on_date_selected(self):
        selected_date = self.calendar.selectedDate()
        sorted_tasks = sorted(self.tasks, key=lambda task: task['date'])
        self.display_tasks(sorted_tasks)

    # Método para adicionar uma tarefa
    def add_task(self):
        task_name = self.task_name_input.text()
        task_desc = self.task_desc_input.text()
        task_time = self.task_time_input.time().toString("hh:mm")
        selected_date = self.calendar.selectedDate()
        if selected_date < QDate.currentDate():
            QMessageBox.warning(self, "Data Inválida", "Não é possível adicionar tarefas no passado.")
        else:
            self.tasks.append({'date': selected_date, 'name': task_name, 'description': task_desc, 'time': task_time})
            self.task_name_input.clear()
            self.task_desc_input.clear()
            self.task_time_input.clear()
            self.display_tasks(self.tasks)

    # Método para remover uma tarefa selecionada
    def remove_selected_task(self):
        selected_items = self.task_viewer.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Nenhuma Tarefa Selecionada", "Selecione uma tarefa para remover.")
        else:
            for item in selected_items:
                index = self.task_viewer.row(item)
                self.tasks.pop(index)
            self.display_tasks(self.tasks)

    # Método para editar uma tarefa
    def edit_task(self, item):
        index = self.task_viewer.row(item)
        task = self.tasks[index]
        task_name = task['name']
        task_desc = task['description']
        task_time = task['time']
        self.task_name_input.setText(task_name)
        self.task_desc_input.setText(task_desc)
        self.task_time_input.setTime(QTime.fromString(task_time, "hh:mm"))

        self.tasks.pop(index)
        self.display_tasks(self.tasks)

    # Método para exibir as tarefas
    def display_tasks(self, tasks):
        self.task_viewer.clear()
        for task in tasks:
            task_item = f"Data: {task['date'].toString('yyyy-MM-dd')}, Nome: {task['name']}, Descrição: {task['description']}, Hora: {task['time']}"
            self.task_viewer.addItem(task_item)

    # Método chamado quando a janela é fechada
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
    app = QApplication(sys.argv)
    task_manager = TaskManagerApp()
    task_manager.show()
    sys.exit(app.exec_())
