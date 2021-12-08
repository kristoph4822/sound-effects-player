import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
from AudioProcessing import AudioProcessing

class App(QApplication):

  def __init__(self, args):
    super(App, self).__init__(args)
    self.mainWindow = MainWindow()
    self.mainWindow.show()
    sys.exit(self.exec_())