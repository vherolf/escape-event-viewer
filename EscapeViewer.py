#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QMainWindow
from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.QtGui import QIcon, QPixmap, QKeySequence,QResizeEvent
from PyQt6.QtCore import Qt
import sys
import PyQt6

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.resize(300, 300)
        self.setWindowTitle("Escape Kiosk")
        
        #self.pixmap = QPixmap('images/fullsize.jpg')
        self.pixmap = QPixmap('images/blue5.png')
        
        self.label = QLabel(self)
        
        self.label.setPixmap(self.pixmap)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.setCentralWidget(self.label)
        
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape.value:
           self.close()


    def resizeEvent(self, e: QResizeEvent) -> None:
        h = self.size().height()
        print( h )
        self.pixmap = self.pixmap.scaledToHeight( h )
        self.label.setPixmap(self.pixmap)

def main():
    app = QApplication(sys.argv)

    window = Window()
    #window.show()
    #window.showMaximized()
    window.showFullScreen()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
