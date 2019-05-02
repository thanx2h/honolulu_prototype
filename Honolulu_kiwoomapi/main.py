import sys
import ViewController as vc
import DataModel as dm

#pyqt8
from PyQt5.QtWidgets import *

class HonoluluAPI():
    def __init__(self):
        print("auto program class!!")
        self.dataModel = dm.DataModel()
        self.viewController = vc.ViewController(self.dataModel)

if __name__ == "__main__":
    print("main execute")
    app = QApplication(sys.argv)
    honoluluApi = HonoluluAPI();
    honoluluApi.viewController.show()
    app.exec_()