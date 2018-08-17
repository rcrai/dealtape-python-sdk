from datetime import datetime

class CallLog(object):

    def __init__(self, url, id, timestamp, staff_id, staff_name=None, customer_id=None, customer_name=None, deal_closed=None):
        self.url = url
        self.id = id
        self.timestamp = timestamp
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.deal_closed = deal_closed

    def to_dict(self):
        timestamp = self.timestamp
        if type(timestamp) is datetime:
            timestamp = int(timestamp.timestamp())
        if type(timestamp) is float:
            timestamp = int(timestamp)
        if type(timestamp) is not int:
            print("Invalid timestamp")
            return None
        return {
            "url": self.url,
            "unique_id": str(self.id),
            "timestamp": timestamp,
            "staff": {
                "id": self.staff_id,
                "name": self.staff_name
            },
            "customer": {
                "id": self.customer_id,
                "name": self.customer_name
            },
            "deal_closed": self.deal_closed
        }
