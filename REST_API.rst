Recurrent.ai DealTape REST API
====================================

单条数据推送:
-------


POST请求(json)

http://data_server.rcrai.com/{business_key}/call/


.. code-block:: python

    {
        "unique_id": "133333333",  // 电话在客户内部系统中的唯一标识
        "url":"http://voice-2.cticloud.cn/05062017/record/7000001/7000001-20170605192458-15302529829-02145994742--record-sip-1-1496661898.303292.mp3", // 电话录音的url
        "timestamp":1484640092, 电话的拨打时间(UNIX时间戳，中国时间)
        "category": "银行业务", // 电话录音类型
        "staff":{
            "name":"张三", // 该电话坐席名称
            "roles":[
                "销售", // 该电话坐席的角色
                "主管"
            ],
            "id": "9999999", // 该电话坐席的唯一标识
            "dept":{
                "name":"特攻一部c组", // 团队名字
                "id": "1206" // 团队唯一标识
            },
            "group": {
                "name": "", // 大组名称
            }
        },
        "customer":{
            "id": "1345" // 客户的唯一标识
            "phone":"xxxxxxx5229",  // 客户电话号码
            "name":"李四",  // 客户的名称
        }
    }

批量数据推送:
-------


POST请求(json)

http://data_server.rcrai.com/{business_key}/call/batch


.. code-block:: python

    {
		"calls": [
			{
			    "unique_id": "133333333",  // 电话在客户内部系统中的唯一标识
			    "url":"http://voice-2.cticloud.cn/05062017/record/7000001/7000001-20170605192458-15302529829-02145994742--record-sip-1-1496661898.303292.mp3", // 电话录音的url
			    "timestamp":1484640092, 电话的拨打时间(UNIX时间戳，中国时间)
			    "category": "银行业务", // 电话录音类型
			    "staff":{
			        "name":"张三", // 该电话坐席名称
			        "roles":[
			            "销售", // 该电话坐席的角色
			            "主管"
			        ],
			        "id": "9999999", // 该电话坐席的唯一标识
			        "dept":{
			            "name":"特攻一部c组", // 团队名字
			            "id": "1206" // 团队唯一标识
			        },
			        "group": {
			            "name": "", // 大组名称
			        }
			    },
			    "customer":{
			        "id": "1345" // 客户的唯一标识
			        "phone":"xxxxxxx5229",  // 客户电话号码
			        "name":"李四",  // 客户的名称
			    }
			},
			{
				"unique_id": "xxxx",
				"url":"https://account.zichan360.com/voice/record/20180911/33_zc360-zz_01012345678_15595178367_20180911142754_1536647274105.wav",
				"timestamp":1536647255,
				"staff":{
				    "name":"申xxx",
				    "roles":["催收员"],
				    "id":"31409"
				},
				"customer":{
				    "id": "xxxx",
				    "phone":"110",
				    "name":"李xxx"
				}
			}
		]
	}

单条语音识别结果获取
-------------

GET请求

http://data_server.rcrai.com/{business_key}/transcript/{unique_id}


.. code-block:: python

    # 成功返回结果
    {
        "source_id": "5b8cde9cd300ca000141013b",
        "results": [
            {
                "begin_time": 0,
                "end_time": 4840,
                "text": "喂，你好，我想问一下。",
                "channel_id": 0
            },
            {
                "begin_time": 4740,
                "end_time": 7750,
                "text": "你这个你这边再和他联系吗？",
                "channel_id": 0
            },
            ...
        ]
    }


.. code-block:: python

    # 识别未完成
    {
        "task_id": "5b8cdee3d300ca0001410146",
        "progress": "PENDING"
    }   

批量语音识别结果获取
-------------

GET请求

http://data_server.rcrai.com/{business_key}/transcript

.. code-block:: python

    # 参数（json):
    {
	    "source_ids": ["id1", "id2"]
    }


.. code-block:: python

    # 成功返回结果
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


单条语义画像获取
-----------

GET请求(json)

http://data_server.rcrai.com/{business_key}/semantic/{unique_id}

.. code-block:: python

    {
        "key": "{access_key_id}", 
        "secret":"{access_key_secret}", 
    }

.. code-block:: python

    # 成功返回结果
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

批量语义画像获取
-----------

POST请求(json)

http://data_server.rcrai.com/{business_key}/semantic

.. code-block:: python

    # 参数(json格式):
    {
        "key": "{access_key_id}", 
        "secret":"{access_key_secret}", 
        "source_ids": ["id1", "id2"]
    }

.. code-block:: python

    # 返回值:
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


