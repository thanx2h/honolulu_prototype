import json

class DataModel:
    def __init__(self):
        print("Data Model!!")
        self.itemList = []

    class ItemInfo:
        def __init__(self, itemCode, itemName):
            self.itemCode = itemCode
            self.itemName = itemName

        def getItemName(self):
            return self.itemName

class ItemHogaInfo:
    def __init__(self):
        self.itemHogaBuySellInfo = {}
        self.itemHogaAllInfo = {}

    def setBuyInfo(self, idx, buyPrice, buyAmount):
        print(str(idx) + " " + buyPrice + " " + buyAmount)
        buyInfo = []
        buyInfo.append(buyPrice)
        buyInfo.append(buyAmount)
        self.itemHogaBuySellInfo["buy"+str(idx)] = buyInfo

    def setSellInfo(self, idx, sellPrice, sellAmount):
        print(str(idx) + " " + sellPrice + " " + sellAmount)
        sellInfo = []
        sellInfo.append(sellPrice)
        sellInfo.append(sellAmount)
        self.itemHogaBuySellInfo["sell"+str(idx)] = sellInfo

    def getItemHogaInfoList(self):
        self.itemHogaBuySellInfo["itemName"] = "테스트종목"
        self.itemHogaAllInfo["All"] = self.itemHogaBuySellInfo
        return self.itemHogaAllInfo

# class ItemHogaInfoEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, ItemHogaInfo):
#             return object.__dict__
#         return json.JSONEncoder.default(self, obj)
