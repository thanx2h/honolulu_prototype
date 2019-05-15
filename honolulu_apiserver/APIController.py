import DataModel as dm

# pyqt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QAxContainer import *
# from PyQt5.QtGui import *
# from datetime import datetime

form_class = uic.loadUiType("main_window.ui")[0]

class APIController(QMainWindow, form_class):
    def __init__(self, model):
        super().__init__()
        self.model = model
        print("View Controller");
        ## kiwoom api init
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.login()

        # kiwoom OpenApi Event Trigger
        self.kiwoom.OnEventConnect.connect(self.event_connect)
        self.kiwoom.OnReceiveRealData.connect(self._OnReceiveRealData)
        self.kiwoom.OnReceiveTrData.connect(self._OnReceiveTrData)

        # 사용 안함
        # self.kiwoom.OnReceiveChejanData.connect(self._OnReceiveChejanData)
        # self.kiwoom.OnReceiveConditionVer.connect(self._OnReceiveConditionVer)
        # self.kiwoom.OnReceiveTrCondition.connect(self._OnReceiveTrCondition)
        # self.kiwoom.OnReceiveRealCondition.connect(self._OnReceiveRealCondition)

        # UI event Trigger
        self.searchItemButton.clicked.connect(self.searchItem)

    def login(self):
        status = self.kiwoom.dynamicCall("GetConnectState()")
        print("login status : " + str(status))

        if status == 0:
            self.kiwoom.dynamicCall("CommConnect()")
        elif status == 1:
            print("already connected")
        self.setupUi(self)

    def getItemList(self):
        try:
            marketList = ["0", "10"]
            for market in marketList:
                codeList = self.kiwoom.dynamicCall("GetCodeListByMarket(QString)", market).split(";")
                for code in codeList:
                    name = self.kiwoom.dynamicCall("GetMasterCodeName(QString)", code)
                    item = dm.DataModel.ItemInfo(code, name)
                    self.model.itemList.append(item)

            # print(self.model.itemList)
        except Exception as e:
            print("getItemList : " + e)

    def searchItem(self, itemName):
        print("insert name : " + itemName)

        itemCode = -9999;

        for item in self.model.itemList:
            if item.itemName == itemName:
                print("code : " + item.itemCode)
                print("name : " + item.itemName)
                dm.DataModel.ItemInfo(item.itemCode, item.itemName)
                # self.getHogaData(item.itemCode)
                itemCode = item.itemCode

        return itemCode

    def getHogaData(self, code):
        print("call getHogaData")
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "종목코드", code)
        print(self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)","주식호가", "opt10004", 0, "0003"));

    # 사용하지 않음
    # def search(self, code):
    #     print("call search")
    #     self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "종목코드", code)
    #     print(self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", "주식기본정보", "opt10001", 0, "0001"));
    #
    # def getChart(self, code):
    #     print("call getChart")
    #     self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "종목코드", code)
    #     today = datetime.today().strftime("%Y%m%d")
    #     print("today : " + today)
    #     self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "기준일자", today)
    #     self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "수정주가구분 ", 0)
    #     print(
    #         self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", "주식일봉차트조회요청", "opt10081", 0, "0002"));

    # 로그인 성공 여부 수신시 이벤트
    def event_connect(self, nErrCode):
        if nErrCode == 0:
            print("login success")
            try:
                self.statusbar.showMessage("login success")
                self.getItemList()
            except Exception as e:
                print(e)
        elif nErrCode == 100:
            print("user data interchange fail")
        elif nErrCode == 101:
            print("server connection fail")
        elif nErrCode == 102:
            print("vision handling fail")

    # Tran 수신시 이벤트
    def _OnReceiveTrData(self, scrNo, rQName, trCode, recordName, prevNext):
        print("call _OnReceiveTrData")
        print(scrNo + " " + rQName + " " + trCode + " " + recordName + " " + prevNext)

        ihi = dm.ItemHogaInfo()

        # 주식 호가
        if trCode == "opt10004":
            buyPrice = self.kiwoom.dynamicCall("GetCommData(QString, QString, int, QString)", trCode, rQName, 0, "매수최우선호가")
            buyAmount = self.kiwoom.dynamicCall("GetCommData(QString, QString, int, QString)", trCode, rQName, 0,"매수최우선잔량")
            ihi.setBuyInfo(1, buyPrice.strip(), buyAmount.strip())

            sellPrice = self.kiwoom.dynamicCall("GetCommData(QString, QString, int, QString)", trCode, rQName, 0, "매도최우선호가")
            sellAmount = self.kiwoom.dynamicCall("GetCommData(QString, QString, int, QString)", trCode, rQName, 0,"매도최우선잔량")
            ihi.setSellInfo(1, sellPrice.strip(), sellAmount.strip())

            for i in range(2, 5):
                buyPrice = self.kiwoom.dynamicCall("GetCommData(QString, QString, int, QString)", trCode, rQName, 0, "매수"+str(i)+"차선호가")
                buyAmount = self.kiwoom.dynamicCall("GetCommData(QString, QString, int, QString)", trCode, rQName, 0, "매수"+str(i)+"차선잔량")
                try:
                    # ihi.setItemHogaList()
                    ihi.setBuyInfo(i, buyPrice.strip(), buyAmount.strip())
                except Exception as e:
                    print(e)
                ihi.setBuyInfo(i, buyPrice.strip(), buyAmount.strip())
                print(str(i) +": " + buyPrice + " " + buyAmount)

                sellPrice = self.kiwoom.dynamicCall("GetCommData(QString, QString, int, QString)", trCode, rQName, 0, "매도"+str(i)+"차선호가")
                sellAmount = self.kiwoom.dynamicCall("GetCommData(QString, QString, int, QString)", trCode, rQName, 0, "매도"+str(i)+"차선잔량")
                ihi.setSellInfo(i,sellPrice.strip(), sellAmount.strip())
                print(str(i) +": " + sellPrice + " " + sellAmount)

                # print(ihi.buyInfo[0])
                # print(ihi.buyInfo[1])
                # print("\n")
                # print(ihi.sellInfo[0])
                # print(ihi.sellInfo[1])

            # nc = NetworkController()
            # nc.requestApiData(buyPriceStr+sellStr)
            try:
                print()
                # ihi.setItemHogaList()
                # self.nc.requestApiData(ihi.getItemHogaInfoList())
            except Exception as e:
                print(e)

    # 실시간 시세 이벤트
    def _OnReceiveRealData(self, jongmokCode, realType, realData):
        print("call _OnReceiveRealData")

    # 사용하지 않음
    # # 수신 메시지 이벤트
    # def _OnReceiveMsg(self, scrNo, rQName, trCode, msg):
    #     print("call 1")
    #
    # # 체결데이터를 받은 시점을 알려준다.
    # # sGubun – 0:주문체결통보, 1:잔고통보, 3:특이신호
    # # sFidList – 데이터 구분은 ‘;’ 이다.
    # def _OnReceiveChejanData(self, gubun, itemCnt, fidList):
    #     print("call 4")
    #
    # # 로컬에 사용자조건식 저장 성공여부 응답 이벤트
    # def _OnReceiveConditionVer(self, ret, msg):
    #     print("call 5")
    #
    # def _OnReceiveTrCondition(self, scrNo, codeList, conditionName, index, next):
    #     print("call 6")
    #
    # def _OnReceiveRealCondition(self, code, type, conditionName, conditionIndex):
    #     print("call 6")

    # def requestApiData(self, data):
    #     url = "http://localhost:8080/v1"
    #     headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    #     data = {'msg': 'hi'}
    #     print(data)
    #     r = requests.post(url, data=json.dumps(data), headers=headers)
