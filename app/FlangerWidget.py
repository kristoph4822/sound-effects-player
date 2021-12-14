from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import QMainWindow, QWidget


class FlangerWidget(QWidget):

    enabled = pyqtSignal()
    changeFrequency = pyqtSignal()
    changeAmplitude = pyqtSignal()
    changeWave = pyqtSignal()

    def __init__(self, parent):
        super(FlangerWidget, self).__init__(parent)

        self.setObjectName("FlangerWidget")
        self.resize(260, 239)
        self.setupUi()

    def setupUi(self):
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 224, 206))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)

        self.enableRadioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.enableRadioButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.enableRadioButton.setObjectName("enableRadioButton")
        self.horizontalLayout_4.addWidget(self.enableRadioButton)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(140, 0))
        self.label_2.setMaximumSize(QtCore.QSize(47, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.frequencyDial = QtWidgets.QDial(self.layoutWidget)
        self.frequencyDial.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frequencyDial.setObjectName("frequencyDial")
        self.frequencyDial.setMinimum(1)
        self.frequencyDial.setMaximum(100)
        self.frequencyDial.setValue(50)
        self.horizontalLayout.addWidget(self.frequencyDial)

        self.frequencyValue = QtWidgets.QLabel(self.layoutWidget)
        self.frequencyValue.setObjectName("frequencyValue")
        self.horizontalLayout.addWidget(self.frequencyValue)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(140, 0))
        self.label_4.setMaximumSize(QtCore.QSize(47, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)

        self.amplitudeDial = QtWidgets.QDial(self.layoutWidget)
        self.amplitudeDial.setMaximumSize(QtCore.QSize(50, 16777215))
        self.amplitudeDial.setObjectName("amplitudeDial")
        self.amplitudeDial.setMinimum(1)
        self.amplitudeDial.setMaximum(100)
        self.amplitudeDial.setValue(10)
        self.horizontalLayout_2.addWidget(self.amplitudeDial)

        self.amplitudeValue = QtWidgets.QLabel(self.layoutWidget)
        self.amplitudeValue.setObjectName("amplitudeValue")
        self.horizontalLayout_2.addWidget(self.amplitudeValue)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.SineRadioButton = QtWidgets.QCheckBox(self.layoutWidget)
        self.SineRadioButton.setObjectName("SineRadioButton")
        self.verticalLayout_2.addWidget(self.SineRadioButton)
        self.SineRadioButton.setChecked(True)

        self.TraingleRadioButton = QtWidgets.QCheckBox(self.layoutWidget)
        self.TraingleRadioButton.setObjectName("TriangleRadioButton")
        self.verticalLayout_2.addWidget(self.TraingleRadioButton)

        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.addConnections()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def addConnections(self):
        self.enableRadioButton.toggled.connect(self.enabled)
        self.frequencyDial.valueChanged.connect(self.changeFrequency)
        self.amplitudeDial.valueChanged.connect(self.changeAmplitude)
        self.SineRadioButton.toggled.connect(self.changeWave)
        self.TraingleRadioButton.toggled.connect(self.changeWave)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("FlangerWidget", "<html><head/><body><p><span style=\" font-weight:600;\">Flanger effect</span></p></body></html>"))
        self.enableRadioButton.setText(_translate("FlangerWidget", "Enable"))
        self.label_2.setText(_translate("FlangerWidget", "Frequency [Hz]"))
        self.frequencyValue.setText(_translate("FlangerWidget", "100"))
        self.label_4.setText(_translate("FlangerWidget", "Amplitude [ms]"))
        self.amplitudeValue.setText(_translate("FlangerWidget", "10"))
        self.label_6.setText(_translate("FlangerWidget", "Wave Type"))
        self.SineRadioButton.setText(_translate("FlangerWidget", "Sine Wave"))
        self.TraingleRadioButton.setText(_translate("FlangerWidget", "Triangular Wave"))
