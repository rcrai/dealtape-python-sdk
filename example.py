from dealtape import CallLog, DealTapeClient
from datetime import datetime

client = DealTapeClient(business="test", endpoint="http://localhost:8001/")
item = CallLog(
    url="CALLLOG_AUDIO_URL", # 电话录音的url
    id="CALLLOG_UNIQUE_IDENTIFIER", # 电话在客户内部系统中的唯一标识
    staff_id="STAFF_ID", # 该电话坐席的唯一标识
    staff_name="STAFF_NAME", # 该电话坐席名称
    staff_roles=["ROLE1", "ROLE2"], # 该坐席的角色 
    staff_dept_id="STAFF_DEPTARTMENT_ID", # 该坐席所在团队ID
    staff_dept_name="STAFF_DEPTARTMENT_NAME", # 该坐席所在团队名称
    staff_group_name="STAFF_GROUP_NAME", # 该坐席所在大组名称
    customer_id="CUSTOMER_ID", # 客户的唯一标识
    customer_name="CUSTOMER_NAME", # 客户的名称
    deal_closed=None, # 该电话是否成单
    timestamp=datetime.now(), # 电话的拨打时间（datetime.datetime类型, 或是int类型的unix时间戳）
    category="AUDIO_CATEGORY" # 电话录音类型
)
resp = client.push_calllog(item)