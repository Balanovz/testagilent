from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from pymeasure.instruments.agilent import Agilent33220A
"""
        wfg.shape = "SINUSOID"          # Sets a sine waveform
        wfg.frequency = 4.7e3           # Sets the frequency to 4.7 kHz
        wfg.amplitude = 1               # Set amplitude of 1 V
        wfg.offset = 0                  # Set the amplitude to 0 V

        wfg.burst_state = True          # Enable burst mode
        wfg.burst_ncycles = 10          # A burst will consist of 10 cycles
        wfg.burst_mode = "TRIGGERED"    # A burst will be applied on a trigger
        wfg.trigger_source = "BUS"      # A burst will be triggered on TRG*

        wfg.output = True               # Enable output of waveform generator
        wfg.trigger()                   # Trigger a burst
        wfg.wait_for_trigger()          # Wait until the triggering is finished
        wfg.beep()                      # "beep"

        wfg.write("voltage?")
        wfg.write("frequency?")
        print(wfg.read())

        print(wfg.check_errors())       # Get the error queue
"""


class Monitoring(QWidget):
    def __init__(self):
        super().__init__()
        self.frequency = None
        self.function = None
        self.voltage = None

        self.update_info()

        self.form_label = QLabel(f"Form signal : {self.function}")
        self.frequency_label = QLabel(f"Frequency : {self.frequency}")
        self.amplitude_label = QLabel(f"Amplitude : {self.voltage}")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.form_label)
        self.layout.addWidget(self.frequency_label)
        self.layout.addWidget(self.amplitude_label)

        self.setLayout(self.layout)

    def update_info(self):
        wfg = Agilent33220A("TCPIP::192.168.1.100::inst0::INSTR")
        wfg.write("function?")
        self.function = wfg.read()
        wfg.write("frequency?")
        self.frequency = wfg.read()
        wfg.write("voltage?")
        self.voltage = wfg.read()
