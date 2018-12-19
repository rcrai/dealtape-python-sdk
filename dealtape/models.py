from datetime import datetime

class CallLog(object):

    def __init__(
        self, url, id, timestamp, 
        staff_id, staff_name=None, staff_roles=None, staff_dept_id=None, staff_dept_name=None, staff_group_name=None, 
        customer_id=None, customer_name=None, 
        title=None,  deal_closed=None, category=None
        ):
        self.url = url
        self.id = id
        self.timestamp = timestamp
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.staff_roles = staff_roles
        self.staff_dept_id = staff_dept_id
        self.staff_dept_name = staff_dept_name
        self.staff_group_name = staff_group_name
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.deal_closed = deal_closed
        self.title = title
        self.category = category

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
            "title": self.title,
            "url": self.url,
            "unique_id": str(self.id),
            "timestamp": timestamp,
            "category": self.category,
            "staff": {
                "id": self.staff_id,
                "name": self.staff_name,
                "roles": self.staff_roles,
                "dept": {
                    "id": self.staff_dept_id,
                    "name": self.staff_dept_name
                },
                "group": {
                    "name": self.staff_group_name
                }
            },
            "customer": {
                "id": self.customer_id,
                "name": self.customer_name
            },
            "deal_closed": self.deal_closed
        }
