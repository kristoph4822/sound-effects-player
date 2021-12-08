from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import QMainWindow, QWidget


class DelayWidget(QWidget):

    enabled = pyqtSignal()
    changeDelay = pyqtSignal()

    def __init__(self, parent):
        super(DelayWidget, self).__init__(parent)

        self.setObjectName("DelayWidget")
        self.resize(276, 142)
        self.setupUi()

    def setupUi(self):
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 222, 88))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.title = QtWidgets.QLabel(self.layoutWidget)
        self.title.setObjectName("title")

        self.horizontalLayout_2.addWidget(self.title, 0, QtCore.Qt.AlignLeft)

        self.enableRadioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.enableRadioButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.enableRadioButton.setObjectName("enableRadioButton")
        self.horizontalLayout_2.addWidget(self.enableRadioButton)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.delayText = QtWidgets.QLabel(self.layoutWidget)
        self.delayText.setMinimumSize(QtCore.QSize(140, 0))
        self.delayText.setMaximumSize(QtCore.QSize(47, 16777215))
        self.delayText.setObjectName("delayText")
        self.horizontalLayout.addWidget(self.delayText)

        self.delayDial = QtWidgets.QDial(self.layoutWidget)
        self.delayDial.setMaximumSize(QtCore.QSize(50, 16777215))
        self.delayDial.setObjectName("delayDial")
        self.delayDial.setMinimum(0)
        self.delayDial.setMaximum(100)
        self.delayDial.setValue(20)
        self.horizontalLayout.addWidget(self.delayDial)

        self.delayValue = QtWidgets.QLabel(self.layoutWidget)
        self.delayValue.setObjectName("delayValue")
        self.horizontalLayout.addWidget(self.delayValue)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.addConnections()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def addConnections(self):
        self.enableRadioButton.toggled.connect(self.enabled)
        self.delayDial.valueChanged.connect(self.changeDelay)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        #self.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("",
                                      "<html><head/><body><p><span style=\" font-weight:600;\">Delay effect</span></p></body></html>"))
        self.enableRadioButton.setText(_translate("DelayWidget", "Enable"))
        self.delayText.setText(_translate("DelayWidget", "Delay [s]"))
        self.delayValue.setText(_translate("DelayWidget", "0.2"))
