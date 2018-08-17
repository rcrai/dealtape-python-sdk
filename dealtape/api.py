import requests


class DealTapeClient(object):
    
    __dtUrl = 'http://data_server.rcrai.com/%s/call'

    def __init__(self, business, auth_key="", auth_secret=""):
        self.business = business
        self.auth_key = auth_key
        self.auth_secret = auth_secret

    def push_calllog(self, calllog):
        data = calllog.to_dict()
        requests.post(self.__dtUrl % self.business, json=data)

    
