import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QWidget, QFileDialog

from DelayWidget import DelayWidget
from PlayerWidget import PlayerWidget
from AudioProcessing import AudioProcessing
from ReverbWidget import ReverbWidget
from FlangerWidget import FlangerWidget
from MplCanvas import MplCanvas
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MainWindow(QMainWindow):
    __slots__ = 'audio_processor'

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.audioProcessor = AudioProcessing()
        self.setObjectName("MainWindow")
        self.resize(800, 800)
        self.setupUi()

    def setupUi(self):
        self.titleWidget = QtWidgets.QWidget(self)
        self.titleWidget.setObjectName("titleWidget")

        self.title = QtWidgets.QLabel(self.titleWidget)
        self.title.setGeometry(QtCore.QRect(320, 20, 126, 23))
        self.title.setObjectName("title")
        self.title.setMinimumWidth(100)

        self.centralWidget = QtWidgets.QWidget(self.titleWidget)
        self.centralWidget.setGeometry(QtCore.QRect(40, 60, 800, 700))
        self.centralWidget.setObjectName("main_widget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("verticalLayout")

        # self.gridLayout = QtWidgets.QGridLayout()
        # self.gridLayout.setObjectName("gridLayout")

        self.delayWidget = DelayWidget(self.centralWidget)
        self.delayWidget.setObjectName("delayWidget")
        self.gridLayout.addWidget(self.delayWidget, 0, 1, 3, 1)

        self.reverbWidget = ReverbWidget(self.centralWidget)
        self.reverbWidget.setObjectName("reverbWidget")
        self.gridLayout.addWidget(self.reverbWidget, 1, 1, 3, 1)

        self.flangerWidget = FlangerWidget(self.centralWidget)
        self.flangerWidget.setObjectName("flangerWidget")
        self.gridLayout.addWidget(self.flangerWidget, 3, 1, 3, 1)

        # self.gridLayout.addLayout(self.gridLayout)
        self.playerWidget = PlayerWidget(self)
        self.playerWidget.setObjectName("playerWidget")
        # self.playerWidget.setMaximumHeight(300)
        # self.playerWidget.setMaximumSize(300,100)
        self.gridLayout.addWidget(self.playerWidget, 0, 0, 3, 1)

        # self.gridLayout.addWidget(QtWidgets.QWidget(self), 2, 1, 2, 1)
        self.sc = MplCanvas(self.audioProcessor.transformed_audio_data)
        self.sc.resize(300, 200)
        self.gridLayout.addWidget(self.sc, 2, 0, 3, 1)
        # self.sc.setGeometry(250,180,500,600)

        self.setCentralWidget(self.titleWidget)

        self.addConnections()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def addConnections(self):
        self.delayWidget.enabled.connect(self.changeDelay)
        self.delayWidget.changeDelay.connect(self.changeDelay)

        self.reverbWidget.enabled.connect(self.changeReverb)
        self.reverbWidget.changeDecay.connect(self.changeReverb)
        self.reverbWidget.changePreDelay.connect(self.changeReverb)
        self.reverbWidget.changeInterval.connect(self.changeReverb)

        self.flangerWidget.enabled.connect(self.changeFlanger)
        self.flangerWidget.changeFrequency.connect(self.changeFlanger)
        self.flangerWidget.changeAmplitude.connect(self.changeFlanger)
        self.flangerWidget.changeWave.connect(self.changeFlanger)
        #self.flangerWidget.changeSineWave.connect(self.setFlangerSineWave)

        self.playerWidget.play.connect(self.playFile)
        self.playerWidget.stop.connect(self.stopFile)
        self.playerWidget.load_file.connect(self.getFile)

    def getFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "Audio files (*.wav `)")[0]
        if len(fname) > 0:
            self.audioProcessor.load_file(fname)
            self.playerWidget.filename.setText(fname)
            self.updateCanvas()

    def playFile(self):
        self.audioProcessor.play()

    def stopFile(self):
        self.audioProcessor.stop()

    def changeDelay(self):
        delay = self.delayWidget.delayDial.value() / 100
        self.delayWidget.delayValue.setText(str(delay))
        if self.delayWidget.enableRadioButton.isChecked():
            self.audioProcessor.add_delay(delay)
        else:
            self.audioProcessor.resetData()

        self.updateCanvas()

    def changeReverb(self):
        decay = self.reverbWidget.decayDial.value() / 100
        predelay = self.reverbWidget.predelayDial.value()
        interval = self.reverbWidget.intervalDial.value()
        self.reverbWidget.decayValue.setText(str(decay))
        self.reverbWidget.predelayValue.setText(str(predelay))
        self.reverbWidget.intervalValue.setText(str(interval))

        if self.reverbWidget.enableRadioButton.isChecked():
            self.audioProcessor.add_reverb(predelay / 1000, decay, interval / 1000)
        else:
            self.audioProcessor.resetData()

        self.updateCanvas()

    def changeFlanger(self):
        freq = self.flangerWidget.frequencyDial.value()
        ampl = self.flangerWidget.amplitudeDial.value()
        wave = "sine" if self.flangerWidget.SineRadioButton.isChecked() else "triangle"
        self.flangerWidget.frequencyValue.setText(str(freq))
        self.flangerWidget.amplitudeValue.setText(str(ampl))

        if self.flangerWidget.enableRadioButton.isChecked():
            self.audioProcessor.add_flanger(freq, ampl/1000, wave)
        else:
            self.audioProcessor.resetData()

        self.updateCanvas()


    def updateCanvas(self):
        self.sc = MplCanvas(self.audioProcessor.transformed_audio_data)
        self.gridLayout.addWidget(self.sc, 2, 0, 3, 1)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Audio Effects</span></p></body></html>"))
