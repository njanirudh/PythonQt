import sys
from PyQt5.QtWidgets import QApplication ,QWidget,QGraphicsScene,QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

#Import the python file created by the pyuic
from Forms.canny_form_ui import Ui_Form

class FormWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()

        # Initialize run after show function so GraphicsView Width,Height values are correct
        self.initializeGraphicsView()

    def initializeGraphicsView(self):
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(QtCore.QRectF(0,0,self.ui.graphicsView.width(),
                                              self.ui.graphicsView.height()))
        self.ui.graphicsView.setScene(self.scene)

    def setImageFromPath(self,path):
        self.imagePixmap = QPixmap(path)
        self.imagePixmap = self.imagePixmap.scaled(int(self.ui.graphicsView.width()),
                                                   int(self.ui.graphicsView.height()))

        self.imageItem = QGraphicsPixmapItem()
        self.imageItem.setPixmap(self.imagePixmap)
        self.imageItem.setPos(0,0)

        self.scene.addItem(self.imageItem)

    def cannyEdgeOnImage(self,value1,value2):
        


if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = FormWidget()
    widget.setImageFromPath("stones.jpg") # Set Image path

    sys.exit(app.exec())