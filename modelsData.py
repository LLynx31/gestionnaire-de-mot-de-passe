from PySide6.QtCore import QSize
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import (QSize, QTime, QUrl, Qt)
from PySide6.QtCore import Signal


class dataAppPass(QLabel):
    clicked = Signal()

    def __init__(self, id_, nomAppOrSite, password):
        super().__init__()
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.id_ = id_
        self.nomAppOrSite = nomAppOrSite
        self.password = password
        self.setText(self.nomAppOrSite)
        self.setMinimumSize(QSize(0, 80))
        self.setMaximumSize(QSize(16777215, 80))

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)



class dataNotePass(QLabel):
    clicked = Signal()

    def __init__(self, id_, noteText):
        super().__init__()
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.id_ = id_
        self.noteText = noteText
        self.setText(self.noteText)
        self.setMinimumSize(QSize(0, 80))
        self.setMaximumSize(QSize(16777215, 80))

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

class dataCB(QLabel):
    clicked = Signal()

    def __init__(self, id_, cbTitulaire, numCB, cvvCB, dateCB):
        super().__init__()
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.id_ = id_
        self.cbTitulaire = cbTitulaire
        self.numCB = numCB
        self.cvvCB = cvvCB
        self.dateCB = dateCB
        self.setText(self.numCB + " " + self.cbTitulaire )
        self.setMinimumSize(QSize(0, 80))
        self.setMaximumSize(QSize(16777215, 80))

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)