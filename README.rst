Recurrent.ai DealTape SDK for Python
====================================


概述
--------

DealTape数据SDK


安装方式
--------

使用PIP进行安装（以Linux系统为例）

.. code-block:: bash
    
    $ pip install -U dealtape

也可以直接安装解压后的安装包

.. code-block:: bash

    $ sudo python setup.py install


快速使用
-------
.. code-block:: python

    # -*- coding: utf-8 -*-
    from dealtape import CallLog, DealTapeClient

    business = 'YOUR_BUSINESS_KEY' # 企业的唯一标识，即在企业DealTape系统中的二级域名
    access_key_id = 'YOUR_ACCESS_KEY_ID' # 企业的AccessKeyId
    access_key_secret = 'YOUR_ACCESS_KEY_SECRET' # 企业的AccessKeySecret
    endpoint = 'http://data_server.rcrai.com/' # api地址

    client = DealTapeClient(business=business, access_key_id=access_key_id, access_key_secret=access_key_secret, endpoint=endpoint)



数据推送
--------
.. code-block:: python

    # 单条推送
    item = CallLog(
        url="CALLLOG_AUDIO_URL", # 电话录音的url
        id="CALLLOG_UNIQUE_IDENTIFIER", # 电话在客户内部系统中的唯一标识
        staff_id="STAFF_ID", # 该电话坐席的唯一标识
        staff_name="STAFF_NAME", # 该电话坐席名称
        staff_roles=["ROLE1", "ROLE2"], # 该坐席的角色 
        staff_dept_id="STAFF_DEPTARTMENT_ID" # 该坐席所在团队ID
        staff_dept_name="STAFF_DEPTARTMENT_NAME" # 该坐席所在团队名称
        staff_group_name="STAFF_GROUP_NAME" # 该坐席所在大组名称
        customer_id="CUSTOMER_ID", # 客户的唯一标识
        customer_name="CUSTOMER_NAME", # 客户的名称
        deal_closed=True/False/None, # 该电话是否成单
        timestamp=TIMESTAMP # 电话的拨打时间（datetime.datetime类型, 或是int类型的unix时间戳）
        category="AUDIO_CATEGORY" # 电话录音类型
    )
    resp = client.push_calllog(item)
    if not resp.ok:
        print(resp.text)

    # 批量推送
    items = [CallLog(
        url="CALLLOG_AUDIO_URL", # 电话录音的url
        id="CALLLOG_UNIQUE_IDENTIFIER", # 电话在客户内部系统中的唯一标识
        staff_id="STAFF_ID", # 该电话坐席的唯一标识
        staff_name="STAFF_NAME", # 该电话坐席名称
        staff_roles=["ROLE1", "ROLE2"], # 该坐席的角色 
        staff_dept_id="STAFF_DEPTARTMENT_ID" # 该坐席所在团队ID
        staff_dept_name="STAFF_DEPTARTMENT_NAME" # 该坐席所在团队名称
        staff_group_name="STAFF_GROUP_NAME" # 该坐席所在大组名称
        customer_id="CUSTOMER_ID", # 客户的唯一标识
        customer_name="CUSTOMER_NAME", # 客户的名称
        deal_closed=True/False/None, # 该电话是否成单
        timestamp=TIMESTAMP # 电话的拨打时间（datetime.datetime类型, 或是int类型的unix时间戳）
        category="AUDIO_CATEGORY" # 电话录音类型
    ), CallLog(...), ...]
    resp = client.push_calllog_batch(items)
    if not resp.ok:
        print(resp.text)
        
    # 返回值
    {
        "status": "OK"
    }


语音识别结果获取
-------------

.. code-block:: python

    # 单条获取
    resp = client.get_transcript(source_id=CALLLOG_UNIQUE_IDENTIFIER) # 电话在客户内部系统中的唯一标识
    if not resp.ok:
        print(resp.text)
    # 返回值
    {
        "results": [
	        {
	            "begin_time": 0,
	            "channel_id": 0,
	            "end_time": 11950,
	            "speaker_type": "s",
	            "text": "喂，喂，你好，我说你儿子xxx到底还不还钱啊？"
	        },
	        ...
	     ]
        "status": "SUCCESS",
        "task_id": "xxxxxxx"
    }

    # 批量获取
    resp = client.get_transcript_batch(source_ids=["id1", "id2"])
    if not resp.ok:
        print(resp.text)
    # 返回值
    {
	    "results": [
	        {
	            "begin_time": 0,
	            "channel_id": 0,
	            "end_time": 11950,
	            "speaker_type": "s",
	            "status": "SUCCESS",
	            "task_id": "xxxxxxx",
	            "text": "喂，喂，你好，我说你儿子xxx到底还不还钱啊？"
	        },
	        {
	            "begin_time": 11850,
	            "channel_id": 0,
	            "end_time": 14180,
	            "speaker_type": "s",
	            "status": "SUCCESS",
	            "task_id": "xxxxxxx",
	            "text": "你直接判他判他刑吧"
	        },
	        ...
	    ],
	    "success": true
	}
        


语义画像获取
-------------

.. code-block:: python

    # 单条获取
    resp = client.get_semantic(source_id=CALLLOG_UNIQUE_IDENTIFIER) # 电话在客户内部系统中的唯一标识
    if not resp.ok:
        print(resp.text)
    # 返回值
    {
	    "entities": [
	        {
	            "briefEvidence": "逾期了几天",
	            "evidence": "我现在跟你说我就我这几天我都逾期了几天呐我一直没联钱我会啊我我这两天我会想办法再还没一点呢就是那慢慢的还进去了我是我...",
	            "mediumEvidence": "我就我这几天我都逾期了几天呐我一直没联钱我",
	            "name": "描述借款信息",
	            "score": 10,
	            "value": "描述借款信息"
	        },
	        {
	            "briefEvidence": "什么时候还",
	            "evidence": "喂你好哎是在家是吧嗯这下啊分买了今天只又可去分天准为什么时候还呀啊你是那个话头慢客服不是我我跟他的房子现在我讲不的听吧还掉的啊还可以尽量就让...",
	            "mediumEvidence": "只又可去分天准为什么时候还呀啊你是那个话头",
	            "name": "协商还款",
	            "score": 35,
	            "value": "协商还款"
	        }
	    ],
	    "status": "SUCCESS",
	    "success": true
	}

    # 批量获取
    resp = client.get_semantic_batch(source_ids=["id1", "id2"])
    if not resp.ok:
        print(resp.text)
    # 返回值
    {
	    "data": {
	        "id1": {
	            "entities": [],
	            "status": "SUCCESS"
	        },
	        "id2": {
	            "entities": [
	                {
	                    "briefEvidence": "逾期了几天",
	                    "evidence": "我现在跟你说我就我这几天我都逾期了几天呐我一直没联钱我会啊我我这两天我会想办法再还没一点呢就是那慢慢的还进去了我是我...",
	                    "mediumEvidence": "我就我这几天我都逾期了几天呐我一直没联钱我",
	                    "name": "描述借款信息",
	                    "score": 10,
	                    "value": "描述借款信息"
	                },
	                {
	                    "briefEvidence": "什么时候还",
	                    "evidence": "喂你好哎是在家是吧嗯这下啊分买了今天只又可去分天准为什么时候还呀啊你是那个话头慢客服不是我我跟他的房子现在我讲不的听吧还掉的啊还可以尽量就让...",
	                    "mediumEvidence": "只又可去分天准为什么时候还呀啊你是那个话头",
	                    "name": "协商还款",
	                    "score": 35,
	                    "value": "协商还款"
	                }
	            ],
	            "status": "SUCCESS"
	        }
	    },
	    "success": true
	}
