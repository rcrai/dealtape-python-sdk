from dealtape import CallLog, DealTapeClient
from datetime import datetime

client = DealTapeClient(business="zichan360")
item = CallLog(
    url="http://xxxx.mp3",
    id="xxxx1",
    staff_id="staff_id",
    customer_id="customer_id",
    deal_closed=False,
    timestamp=datetime.now()
    )
resp = client.push_calllog(item)