import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication ,QWidget,QPushButton

# Simple Custom widget with a Button
class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("My Widget")

        #Loading the '.ui. form and displaying it
        self.ui = uic.loadUi('Forms/canny_form.ui', self)

        #Access the ui components by name and connect the signals to the slots
        self.ui.processButton.clicked.connect(self.onProcessButtonClicked)
        self.ui.clearButton.clicked.connect(self.onClearButtonClicked)

        self.show()

    # Slots for button
    def onProcessButtonClicked(self):
        print("Process Button is clicked")

    def onClearButtonClicked(self):
        print("Clear Button is clicked")

if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())