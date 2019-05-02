#pyqt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QAxContainer import *
from PyQt5.QtGui import *

class DataModel:
    def __init__(self):
        print("Data Model!!")
        self.itemList = []


    class ItemInfo:
        def __init__(self, itemCode, itemName):
            self.itemCode = itemCode
            self.itemName = itemName


