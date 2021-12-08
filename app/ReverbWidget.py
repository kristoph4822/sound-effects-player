from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import QMainWindow, QWidget


class ReverbWidget(QWidget):

    enabled = pyqtSignal()
    changeDecay = pyqtSignal()
    changePreDelay = pyqtSignal()
    changeInterval = pyqtSignal()

    def __init__(self, parent):
        super(ReverbWidget, self).__init__(parent)

        self.setObjectName("ReverbWidget")
        self.resize(276, 142)
        self.setupUi()

    def setupUi(self):

        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(40, 30, 222, 204))
        self.widget.setObjectName("widget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.title = QtWidgets.QLabel(self.widget)
        self.title.setObjectName("title")
        self.horizontalLayout_4.addWidget(self.title)

        self.enableRadioButton = QtWidgets.QRadioButton(self.widget)
        self.enableRadioButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.enableRadioButton.setObjectName("enableRadioButton")
        self.horizontalLayout_4.addWidget(self.enableRadioButton)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.decayText = QtWidgets.QLabel(self.widget)
        self.decayText.setMinimumSize(QtCore.QSize(140, 0))
        self.decayText.setMaximumSize(QtCore.QSize(47, 16777215))
        self.decayText.setObjectName("decayText")
        self.horizontalLayout.addWidget(self.decayText)

        self.decayDial = QtWidgets.QDial(self.widget)
        self.decayDial.setMaximumSize(QtCore.QSize(50, 16777215))
        self.decayDial.setObjectName("decayDial")
        self.decayDial.setMinimum(10)
        self.decayDial.setMaximum(400)
        self.decayDial.setValue(398)
        self.horizontalLayout.addWidget(self.decayDial)

        self.decayValue = QtWidgets.QLabel(self.widget)
        self.decayValue.setObjectName("decayValue")
        self.horizontalLayout.addWidget(self.decayValue)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.predelayText = QtWidgets.QLabel(self.widget)
        self.predelayText.setMinimumSize(QtCore.QSize(140, 0))
        self.predelayText.setMaximumSize(QtCore.QSize(47, 16777215))
        self.predelayText.setObjectName("predelayText")
        self.horizontalLayout_2.addWidget(self.predelayText)

        self.predelayDial = QtWidgets.QDial(self.widget)
        self.predelayDial.setMaximumSize(QtCore.QSize(50, 16777215))
        self.predelayDial.setObjectName("predelayDial")
        self.predelayDial.setMinimum(0)
        self.predelayDial.setMaximum(500)
        self.predelayDial.setValue(500)
        self.horizontalLayout_2.addWidget(self.predelayDial)

        self.predelayValue = QtWidgets.QLabel(self.widget)
        self.predelayValue.setObjectName("predelayValue")
        self.horizontalLayout_2.addWidget(self.predelayValue)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.intervalText = QtWidgets.QLabel(self.widget)
        self.intervalText.setMinimumSize(QtCore.QSize(140, 0))
        self.intervalText.setMaximumSize(QtCore.QSize(47, 16777215))
        self.intervalText.setObjectName("diffusionText")
        self.horizontalLayout_3.addWidget(self.intervalText)

        self.intervalDial = QtWidgets.QDial(self.widget)
        self.intervalDial.setMaximumSize(QtCore.QSize(50, 16777215))
        self.intervalDial.setObjectName("diffusionDial")
        self.intervalDial.setMinimum(0)
        self.intervalDial.setMaximum(500)
        self.intervalDial.setValue(500)
        self.horizontalLayout_3.addWidget(self.intervalDial)

        self.intervalValue = QtWidgets.QLabel(self.widget)
        self.intervalValue.setObjectName("diffusionValue")
        self.horizontalLayout_3.addWidget(self.intervalValue)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.addConnections()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def addConnections(self):
        self.enableRadioButton.toggled.connect(self.enabled)
        self.decayDial.valueChanged.connect(self.changeDecay)
        self.predelayDial.valueChanged.connect(self.changePreDelay)
        self.intervalDial.valueChanged.connect(self.changeInterval)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("ReverbWidget", "<html><head/><body><p><span style=\" font-weight:600;\">Reverb effect</span></p></body></html>"))
        self.enableRadioButton.setText(_translate("ReverbWidget", "Enable"))
        self.decayText.setText(_translate("ReverbWidget", "Decay time [s]"))
        self.decayValue.setText(_translate("ReverbWidget", "4.0"))
        self.predelayText.setText(_translate("ReverbWidget", "Pre-delay [ms]"))
        self.predelayValue.setText(_translate("ReverbWidget", "500"))
        self.intervalText.setText(_translate("ReverbWidget", "Reflections interval [ms]"))
        self.intervalValue.setText(_translate("ReverbWidget", "500"))
