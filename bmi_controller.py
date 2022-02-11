from PyQt5 import QtCore


class BmiController:
    def __init__(self, window, model):
        self.window = window
        self.dataModel = model
        self.configure_bounds(self.window)
        self.connect_events(self.window)
        self.init_values(self.window)

    def configure_bounds(self, window):
        # Tallest person on record is ~275cm
        window.set_bounds(window.spin_height, 1, 300)
        # Heaviest person on record is ~650kg
        window.set_bounds(window.spin_weight, 1, 1000)

    def connect_events(self, window):
        window.spin_height.valueChanged.connect(self.set_height)
        window.spin_weight.valueChanged.connect(self.set_weight)
        self.display_bmi()

    def init_values(self, window):
        _ = QtCore.QCoreApplication.translate
        window.spin_height.setValue(self.dataModel.height)
        window.spin_weight.setValue(self.dataModel.weight)
        self.display_bmi()

    def set_height(self):
        self.dataModel.set_height(self.window.spin_height.value())
        self.display_bmi()

    def set_weight(self):
        self.dataModel.set_weight(self.window.spin_weight.value())
        self.display_bmi()

    def display_bmi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.line_output.setText(
            _translate("MainWindow", self.dataModel.get_bmi())
        )
