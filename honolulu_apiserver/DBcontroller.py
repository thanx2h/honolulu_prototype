import redis

class DBController:

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
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    def setData(self, key, value):
        print("dbc, setData : " + key + " " + value)
        self.r.set(key, value)

    def getData(self, key):
        print("dbc, getData")
        return self.r.get(key);