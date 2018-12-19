import requests


DEFUALT_ENDPOINT = 'http://data_server.rcrai.com/'


class DealTapeClient(object):
    

    def __init__(self, business, access_key_id="", access_key_secret="", endpoint=None):
        if not endpoint:
            self.endpoint = DEFUALT_ENDPOINT
        else:
            self.endpoint = endpoint.strip("/") + "/"
        self.business = business
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret

    def push_calllog(self, calllog):
        data = calllog.to_dict()
        resp = requests.post(self.endpoint + "%s/call/" % self.business, json=data)
        return resp

    def get_transcript(self, source_id):
        resp = requests.get(self.endpoint + "%s/transcript/%s" % (self.business, source_id))
        return resp
    
    def get_semantic(self, source_id):
        resp = requests.post(self.endpoint + "%s/semantic/%s" % (self.business, source_id), json={
            "key": self.access_key_id,
            "secret": self.access_key_secret
        })
        return resp