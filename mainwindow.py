from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from pymeasure.instruments.agilent import Agilent33220A
from tablewidget import TableWidget
from header import Header


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Test project"
        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 300
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # adding widgets to the mainwindow
        self.table_widget = TableWidget()
        self.header_widget = Header()
        union_widget = QWidget()
        v_layout = QVBoxLayout(union_widget)
        v_layout.addWidget(self.header_widget)
        v_layout.addWidget(self.table_widget)
        self.setCentralWidget(union_widget)

        self.show()
