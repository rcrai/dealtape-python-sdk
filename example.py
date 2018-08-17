from dealtape import CallLog, DealTapeClient
from datetime import datetime

client = DealTapeClient(business="rcrai")
item = CallLog(
    url="http://xxxx.mp3",
    id="xxxx",
    staff_id="staff_id",
    customer_id="customer_id",
    deal_closed=False,
    timestamp=datetime.now()
    )
client.push_calllog(item)