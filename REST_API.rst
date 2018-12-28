Recurrent.ai DealTape REST API
====================================

单条数据推送:
-------


POST请求(json)

http://data_server.rcrai.com/{business_key}/call/


.. code-block:: python

    {
        "source_id": "133333333",  // 电话在客户内部系统中的唯一标识
        "url":"http://xxxx.cn/xxxxxx.mp3", // 电话录音的url
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
		"data": [
			{
			    "source_id": "133333333",  // 电话在客户内部系统中的唯一标识
			    "url":"http://xxxxx.cn/xxxxxx.mp3", // 电话录音的url
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
				"source_id": "xxxx",
				"url":"https://xxxxx.com/xxxxx.wav",
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

.. code-block:: python

    # 返回结果
    {
	    "failed_ids": [],  # 失败的source_id列表
	    "status": "OK",
	    "succeed_ids": [  # 成功的source_id列表
	        "42221378094341301536649453",
	        "42221378094263871536647253"
	    ]
	}

单条语音识别结果获取
-------------

GET请求

http://data_server.rcrai.com/{business_key}/transcript/{source_id}


.. code-block:: python

    # 成功返回结果
    {
        "source_id": "5b8cde9cd300ca000141013b",
        "segments": [
            {
                "begin_time": 0, // 句子开始时间
                "end_time": 4840, // 句子结束时间
                "text": "喂，你好，我想问一下。", // 句子文本内容
                "channel_id": 0   // channel id 0为坐席，1为客户
                "speaker_type": "s", // speaker type s为坐席，c为客户
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


.. code-block:: python

    # 识别未完成
    {
        "source_id": "5b8cdee3d300ca0001410146",
        "status": "PENDING"
    }   

.. code-block:: python

    # 识别出错
    {
        "source_id": "5b8cdee3d300ca0001410146",
        "status": "FAILED",
        "message": "音频文件下载失败", 
        "code": 20200
    }   

错误类型

- 20104: '音频数据不存在'
- 20105: '音频文件下载失败'
- 20106: '音频文件错误'
- 20107: '音频文件太短'
- 20108: '音频文件太长'
- 20200: '特征抽取失败' 
- 20201: '说话人分割失败'
- 20202: '语音转文本失败'



批量语音识别结果获取
-------------

POST请求

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
            {
                "source_id": "id1",
                "segments": [
                    {
                        "begin_time": 0, // 句子开始时间
                        "end_time": 4840, // 句子结束时间
                        "text": "喂，你好，我想问一下。", // 句子文本内容
                        "channel_id": 0   // channel id 0为坐席，1为客户
                        "speaker_type": "s", // speaker type s为坐席，c为客户
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
            },
            {
                "source_id": "id2",
                "segments": [
                    {
                        "begin_time": 0, // 句子开始时间
                        "end_time": 4840, // 句子结束时间
                        "text": "喂，你好，我想问一下。", // 句子文本内容
                        "channel_id": 0   // channel id 0为坐席，1为客户
                        "speaker_type": "s", // speaker type s为坐席，c为客户
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
            },
        }
	}


单条语义画像获取
-----------

GET请求(json)

http://data_server.rcrai.com/{business_key}/semantic/{source_id}


.. code-block:: python

    # 成功返回结果
    {
        "entities": [
            {
                "name": "身份确认",
                "value": "身份确认", // 语义点
                "evidence": "嗯喂，你好，是是吗？喂你好， 你好，唉，你", // 语义点证据
                "mediumEvidence": "",
                "score": 0
            },
            {
                "name": "身份确认",
                "value": "身份确认",
                "evidence": "话能嗯对，堂哥 您是他堂哥是吗？喂，嗯，那你这",
                "mediumEvidence": "",
                "score": 0
            },
            ...
        ],
	    "status": "SUCCESS"
	}

批量语义画像获取
-----------

POST请求(json)

http://data_server.rcrai.com/{business_key}/semantic

.. code-block:: python

    # 参数(json格式):
    {
        "source_ids": ["id1", "id2"]  // 客户传过来的source_id
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
	                    "evidence": "我现在跟你说我就我这几天我都逾期了几天呐我一直没联钱我会啊我我这两天我会想...",
	                    "medium_evidence": "我就我这几天我都逾期了几天呐我一直没联钱我",
	                    "name": "描述借款信息",
	                    "score": 10,
	                    "value": "描述借款信息"
	                },
	                {
	                    "brief_evidence": "什么时候还",
	                    "evidence": "喂你好哎是在家是吧嗯这下啊分买了今天只又可去分天准为什么时候还呀...",
	                    "medium_evidence": "只又可去分天准为什么时候还呀啊你是那个话头",
	                    "name": "协商还款",
	                    "score": 35,
	                    "value": "协商还款"
	                }
                    ...
	            ],
	            "source_id": "id2",
	            "status": "SUCCESS"
	        }
	    ],
	}


