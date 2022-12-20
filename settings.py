from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QDoubleSpinBox


class Settings(QWidget):
    def __init__(self):
        super().__init__()
        v_layout = QVBoxLayout()

        self.func_label = QLabel("Form signal : ")
        self.ampl_label = QLabel("Amplitude : ")
        self.freq_label = QLabel("Frequency : ")
        self.func_combox = QComboBox()
        self.ampl_ds = QDoubleSpinBox()
        self.freq_ds = QDoubleSpinBox()

        self.func_combox.addItems(["sin", "sqare", "ramp", "pulse", "noise", "arb"])
        self.ampl_ds.setMinimum(0)
        self.ampl_ds.setMaximum(20)
        self.freq_ds.setMinimum(0)
        self.freq_ds.setMaximum(5999999)

        self.func_layout = QHBoxLayout()
        self.func_layout.addWidget(self.func_label)
        self.func_layout.addWidget(self.func_combox)

        self.ampl_layout = QHBoxLayout()
        self.ampl_layout.addWidget(self.ampl_label)
        self.ampl_layout.addWidget(self.ampl_ds)

        self.freq_layout = QHBoxLayout()
        self.freq_layout.addWidget(self.freq_label)
        self.freq_layout.addWidget(self.freq_ds)

        for i in [self.func_layout, self.ampl_layout, self.freq_layout]:
            v_layout.addLayout(i)

        self.setLayout(v_layout)
