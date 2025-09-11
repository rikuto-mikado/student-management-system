from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QMainWindow,
)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        file_manu_item = sse


app = QApplication(sys.argv)
age_calcurator = MainWindow()
age_calcurator.show()
sys.exit(app.exec())
