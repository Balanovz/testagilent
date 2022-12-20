from PySide6.QtWidgets import QTabWidget, QVBoxLayout, QWidget
from settings import Settings
from monitoring import Monitoring


class TableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        # initialize tab screen
        self.tabs = QTabWidget()

        self.monitoring_tab = Monitoring()
        self.settings = Settings()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tabs.resize(300, 200)
        
        # Add tabs
        self.tabs.addTab(self.monitoring_tab, "Monitoring")
        self.tabs.addTab(self.settings, "Settings")
        self.tabs.addTab(self.tab3, "Tab 3")
        self.tabs.addTab(self.tab4, "Tab 4")
        
        # Add tabs
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        