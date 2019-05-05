import json

class DataModel:
    def __init__(self):
        print("Data Model!!")
        self.itemList = []

    class ItemInfo:
        def __init__(self, itemCode, itemName):
            self.itemCode = itemCode
            self.itemName = itemName


class ItemHogaInfo:
    def __init__(self):
        self.itemHogaInfoList = {}

    def setBuyInfo(self, idx, buyPrice, buyAmount):
        print(str(idx) + " " + buyPrice + " " + buyAmount)
        buyInfo = []
        buyInfo.append(buyPrice)
        buyInfo.append(buyAmount)
        self.itemHogaInfoList["buy"+str(idx)] = buyInfo

    def setSellInfo(self, idx, sellPrice, sellAmount):
        print(str(idx) + " " + sellPrice + " " + sellAmount)
        sellInfo = []
        sellInfo.append(sellPrice)
        sellInfo.append(sellAmount)
        self.itemHogaInfoList["sell"+str(idx)] = sellInfo

# class ItemHogaInfoEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, ItemHogaInfo):
#             return object.__dict__
#         return json.JSONEncoder.default(self, obj)
