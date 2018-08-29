import requests


class DealTapeClient(object):
    
    __dtUrl = 'http://data_server.rcrai.com/'

    def __init__(self, business, auth_key="", auth_secret=""):
        self.business = business
        self.auth_key = auth_key
        self.auth_secret = auth_secret

    def push_calllog(self, calllog):
        data = calllog.to_dict()
        resp = requests.post(self.__dtUrl + "%s/call/" % self.business, json=data)
        return resp

    def get_transcript(self, source_id):
        resp = requests.get(self.__dtUrl + "%s/transcript/%s" % (self.business, source_id))
        return resp
    