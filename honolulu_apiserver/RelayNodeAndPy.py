# import requests
# import json
# # from Utils import JsonUtils as ju
# import DataModel as dm
#
# class NetworkController:
#     def __init__(self):
#         self.url = "http://localhost:8080/v1"
#         self.data =  {'msg': 'Hi!!!'}
#         self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#
#     def requestApiData(self, data):
#         try:
#             print(data)
#             print("json.dumps(data) : " + json.dumps(data))
#         except Exception as e:
#             print(e)
#
#         r = requests.post(self.url, data=json.dumps(data), headers=self.headers)
#
#     def responseApiData(self, data):
#         pass
