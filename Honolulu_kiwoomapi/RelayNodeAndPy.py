import requests
import json
# import Adafruit_DHT as dht
# h,t = dht.read_retry(dht.DHT22, 4)
# print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(t, h)

class RelayNodeAndPy:
    def __init__(self):
        self.url = "http://localhost:8080/api"
        self.data =  {'msg': 'Hi!!!'}
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        self.requestApiData(self.data)

    def requestApiData(self, data):
        print(data)
        r = requests.post(self.url, data=json.dumps(data), headers=self.headers)