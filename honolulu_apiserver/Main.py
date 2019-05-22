# -- coding: utf-8 --
from flask import Flask
from flask_restful import Resource, Api, reqparse
import threading
from flask_cors import CORS

import APIController as ac
import DataModel as dm
from kiwoomMain import KiwoomAPI

import json
import sys

#pyqt8
from PyQt5.QtWidgets import *

app = Flask(__name__)
api = Api(app)

cors = CORS(app, resources={
  r"/v1/*": {"origin": "*"},
  r"/api/*": {"origin": "*"},
})

parser = reqparse.RequestParser()
parser.add_argument('itemName', type=str)

@app.route("/v1/getItemCode", methods=['GET'])
def getItemCode():
    args = parser.parse_args()
    print(args['itemName'])
    returnData = APIServer.instance().apiController.searchItem(args['itemName'])
    print(returnData)
    result = []
    if returnData == -9999:
        result.append("Fail. There is no itemCode")
    else:
        result.append("Success")
        result.append(returnData)

    return json.dumps(result)

@app.route("/v1/getHogaData", methods=['POST'])
def getHogaData():
    print("getHogaData : " + json.dumps(dm.ItemHogaInfo.instance().getitemHogaAllInfo()))
    return json.dumps(dm.ItemHogaInfo.instance().getitemHogaAllInfo())

class APIServer():
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
        print("API Sever Start!")
        self.dataModel = dm.DataModel()
        self.ItemHogaInfo = dm.ItemHogaInfo();
        self.apiController = ac.APIController(self.dataModel)

# def custom_call():
#     print(custom_call())
#
# class CustomServer(Server):
#     def __call__(self, app, *args, **kwargs):
#         custom_call()
#         #Hint: Here you could manipulate app
#         return Server.__call__(self, app, *args, **kwargs)
#
# app = Flask(__name__)
# manager = Manager(app)
#
# # Remeber to add the command to your Manager instance
# manager.add_command('runserver', CustomServer())
#
# if __name__ == "__main__":
#     manager.run()

# manager = Manager(app)
#
# def crazy_call():
#     print("crazy_call")
#
# @manager.command
# def runserver():
#     app.run()
#     crazy_call()
#
# if __name__ == "__main__":
#     manager.run()

def start_kiwoomapi():
    def kiwoomapi():
        print("kiwoomapi")
        app = QApplication(sys.argv)
        kiwoomAPI = KiwoomAPI();
        APIServer.instance().apiController.show()
        app.exec_()
    thread = threading.Thread(target=kiwoomapi)
    thread.start()

if __name__ == "__main__":
    start_kiwoomapi()
    app.run(host='localhost', port=5000)


