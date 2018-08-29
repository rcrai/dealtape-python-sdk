import requests


class DealTapeClient(object):
    
    __dtUrl = 'http://data_server.rcrai.com/'

    def __init__(self, business, access_key_id="", access_key_secret=""):
        self.business = business
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret

    def push_calllog(self, calllog):
        data = calllog.to_dict()
        resp = requests.post(self.__dtUrl + "%s/call/" % self.business, json=data)
        return resp

    def get_transcript(self, source_id):
        resp = requests.get(self.__dtUrl + "%s/transcript/%s" % (self.business, source_id))
        return resp
    
    def get_semantic(self, source_id):
        resp = requests.post(self.__dtUrl + "%s/semantic/%s" % (self.business, source_id), json={
            "key": self.access_key_id,
            "secret": self.access_key_secret
        })
        return resp