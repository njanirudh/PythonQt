# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication ,QWidget

#Import the python file created by the pyuic
from Forms.canny_form_ui import Ui_Form

class FormWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = FormWidget()
    widget.show()

    sys.exit(app.exec())