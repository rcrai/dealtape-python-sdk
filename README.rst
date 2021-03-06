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
	    "failed_ids": [],  # 失败的unique_id列表
	    "status": "OK",
	    "succeed_ids": [  # 成功的unique_id列表
	        "42221378094341301536649453",
	        "42221378094263871536647253"
	    ]
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
        "source_id": "5b8cde9cd300ca000141013b",
        "results": [
            {
                "begin_time": 0, // 句子开始时间
                "end_time": 4840, // 句子结束时间
                "text": "喂，你好，我想问一下。", // 句子文本内容
                "channel_id": 0   // channel id 0为坐席，1为客户
            },
            {
                "begin_time": 4740,
                "end_time": 7750,
                "text": "你这个你这边再和他联系吗？",
                "channel_id": 0
            },
            ...
        ]
        "status": "SUCCESS"
    }

    # 批量获取
    resp = client.get_transcript_batch(source_ids=["id1", "id2"])
    if not resp.ok:
        print(resp.text)
    # 返回值
    {
	    "results": [
	        [
	            {
	                "begin_time": 0,
	                "channel_id": 0,
	                "end_time": 11950,
	                "source_id": "id1",  # 传入的id1
	                "speaker_type": "s",
	                "status": "SUCCESS",
	                "text": "喂，喂，你好，我说你儿子李龙到底还不还钱啊？"
	            },
	            ...
	        ],
	        [
	            {
	                "begin_time": 0,
	                "channel_id": 1,
	                "end_time": 1340,
	                "source_id": "id2",  # 传入的id2
	                "speaker_type": "c",
	                "status": "SUCCESS",
	                "text": "喂你好"
	            },
	            ...
	        ]
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
        "results": [
	        {
	            "source_id": "id1",
	            "entities": [
			        {
			            "brief_evidence": "逾期了几天",
			            "evidence": "我现在跟你说我就我这几天我都逾期了几天呐我一直没联钱我会啊我我这两天我会想办法再还没一点呢就是那慢慢的还进去了我是我...",
			            "medium_evidence": "我就我这几天我都逾期了几天呐我一直没联钱我",
			            "name": "描述借款信息",
			            "score": 10,
			            "value": "描述借款信息"
			        },
			        {
			            "brief_evidence": "什么时候还",
			            "evidence": "喂你好哎是在家是吧嗯这下啊分买了今天只又可去分天准为什么时候还呀啊你是那个话头慢客服不是我我跟他的房子现在我讲不的听吧还掉的啊还可以尽量就让...",
			            "medium_evidence": "只又可去分天准为什么时候还呀啊你是那个话头",
			            "name": "协商还款",
			            "score": 35,
			            "value": "协商还款"
			        }
			    ],
			    "status": "SUCCESS",
			 },
        ],
	    "success": true
	}

    # 批量获取
    resp = client.get_semantic_batch(source_ids=["id1", "id2"])
    if not resp.ok:
        print(resp.text)
    # 返回值
    {
	    "results": [
	        {
	            "entities": [],
	            "source_id": "id1",
	            "status": "SUCCESS"
	        },
	        {
	            "entities": [
	                {
	                    "brief_evidence": "逾期了几天",
	                    "evidence": "我现在跟你说我就我这几天我都逾期了几天呐我一直没联钱我会啊我我这两天我会想办法再还没一点呢就是那慢慢的还进去了我是我...",
	                    "medium_evidence": "我就我这几天我都逾期了几天呐我一直没联钱我",
	                    "name": "描述借款信息",
	                    "score": 10,
	                    "value": "描述借款信息"
	                },
	                {
	                    "brief_evidence": "什么时候还",
	                    "evidence": "喂你好哎是在家是吧嗯这下啊分买了今天只又可去分天准为什么时候还呀啊你是那个话头慢客服不是我我跟他的房子现在我讲不的听吧还掉的啊还可以尽量就让...",
	                    "medium_evidence": "只又可去分天准为什么时候还呀啊你是那个话头",
	                    "name": "协商还款",
	                    "score": 35,
	                    "value": "协商还款"
	                }
	            ],
	            "source_id": "id2",
	            "status": "SUCCESS"
	        }
	    ],
	    "success": true
	}


创建交易信息
-------------

.. code-block:: python

    resp = client.create_dealinfo({
        # 客户ID, 不允许为空，string类型
        "customer_id": "xxx",
        # 成交产品名称, 不允许为空，string类型
        "product_name": "xxx",
        # 成交产品ID, 不允许为空，string类型
        "product_id": "xxx",
        # 成交时间, 不允许为空, string类型， 格式为"yyyy-mm-dd HH:MM:SS"或者”yyyy-mm-dd“
        "deal_time": "2019-01-01 09:01:01",
        # 到期时间, 不允许为空, string类型，格式同deal_time
        "expire_time": "2019-01-02",
        # 跟进销售工号, 不允许为空，string类型
        "staff_no": "123"
    })

    if not resp.ok:
        print(resp.text)

    # 返回值
    {
        "message": "ok",
        "success": true
    }