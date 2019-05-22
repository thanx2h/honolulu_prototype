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
    _instance = None

    @classmethod
    def _getInstance(cls):
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._getInstance
        return cls._instance

    def __init__(self):
        self.itemHogaBuySellInfo = {}
        self.itemHogaAllInfo = {}
        self.buyInfoList = []
        self.sellInfoList = []

    def clearData(self):
        self.itemHogaBuySellInfo.clear();
        self.itemHogaAllInfo.clear()
        self.buyInfoList.clear()
        self.sellInfoList.clear()

    def setBuyInfo(self, idx, buyPrice, buyAmount):
        print(str(idx) + " " + buyPrice + " " + buyAmount)
        buyInfo = []
        buyInfo.append(buyPrice)
        buyInfo.append(buyAmount)
        self.buyInfoList.append(buyInfo)

    def setSellInfo(self, idx, sellPrice, sellAmount):
        print(str(idx) + " " + sellPrice + " " + sellAmount)
        sellInfo = []
        sellInfo.append(sellPrice)
        sellInfo.append(sellAmount)
        self.sellInfoList.append(sellInfo)

    def setitemHogaAllInfo(self):
        self.itemHogaBuySellInfo["itemName"] = "테스트종목"
        self.itemHogaBuySellInfo["buy"] = self.buyInfoList
        self.itemHogaBuySellInfo["sell"] = self.sellInfoList
        self.itemHogaAllInfo["All"] = self.itemHogaBuySellInfo

    def getitemHogaAllInfo(self):
        return self.itemHogaAllInfo


# class ItemHogaInfoEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, ItemHogaInfo):
#             return object.__dict__
#         return json.JSONEncoder.default(self, obj)
