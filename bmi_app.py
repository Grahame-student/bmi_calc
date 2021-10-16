from PyQt5 import QtWidgets

from bmi_calculator import BmiCalc
from bmi_controller import BmiController
from main import UiMainWindow


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(main_window)
    controller = BmiController(ui, BmiCalc(1, 1))
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
