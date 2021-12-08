from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import QMainWindow, QWidget
import numpy as np
import matplotlib
matplotlib.use('QT5Agg')

import matplotlib.pylab as plt

from MplCanvas import MplCanvas


class PlayerWidget(QWidget):

    play = pyqtSignal()
    stop = pyqtSignal()
    load_file = pyqtSignal()

    def __init__(self, parent):
        super(PlayerWidget, self).__init__(parent)

        self.setObjectName("PlayerWidget")
        self.resize(300, 125)
        self.setupUi()

    def setupUi(self):

        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(21, 20, 300, 121))
        self.widget.setObjectName("widget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.playButton = QtWidgets.QPushButton(self.widget)
        self.playButton.setObjectName("playButton")
        self.verticalLayout.addWidget(self.playButton)

        self.stopButton = QtWidgets.QPushButton(self.widget)
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout.addWidget(self.stopButton)

        self.loadFileButton = QtWidgets.QPushButton(self.widget)
        self.loadFileButton.setObjectName("loadFileButton")
        self.verticalLayout.addWidget(self.loadFileButton)

        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)

        self.filename = QtWidgets.QLabel(self.widget)
        self.filename.setObjectName("filname")
        self.verticalLayout_2.addWidget(self.filename)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.addConnections()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def addConnections(self):
        self.playButton.clicked.connect(self.play)
        self.stopButton.clicked.connect(self.stop)
        self.loadFileButton.clicked.connect(self.load_file)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.playButton.setText(_translate("PlayerWidget", "Play"))
        self.stopButton.setText(_translate("PlayerWidgetForm", "Stop"))
        self.loadFileButton.setText(_translate("PlayerWidget", "Load .wav file"))
        self.label.setText(_translate("PlayerWidget", "Current file:"))
        self.filename.setText(_translate("PlayerWidget", "piano.wav"))