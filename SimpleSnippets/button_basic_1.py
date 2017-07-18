import sys
from PyQt5.QtWidgets import QApplication ,QWidget,QPushButton

# Simple Custom widget with a Button
class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("My Widget")

        # Setting the basic size and parameters of the button
        button = QPushButton("Start",self)
        button.resize(100,30)
        button.move((self.width()/2 - button.width()/2)
                    ,self.height()/2 - button.height()/2)

        #Button onClicked 'Signal' connected to our 'Slot'
        button.clicked.connect(self.clickMethod)

        #Set default size of the Widget
        self.show()

    def clickMethod(self):
        print("Start Button is clicked")

if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = MyWidget()
    sys.exit(app.exec())