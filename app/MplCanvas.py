import sys
import matplotlib

matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, data, parent=None, width=8, height=4, dpi=20):
        fig = Figure(figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(fig)
        self.axes = fig.add_subplot(111)
        self.axes.plot(np.arange(0, len(data)),data)

