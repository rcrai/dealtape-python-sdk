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
        "task_id": "5b8cde9cd300ca000141013b",
        "results": [
            {
                "begin_time": 0, // 句子开始时间
                "end_time": 4840, // 句子结束时间
                "text": "喂，你好，我想问一下。", // 句子文本内容
                "channel_id": 0   // channel id 0为坐席，1为客户
                "speaker_type": "s", // speaker type s为坐席，c为客户
            },
           ...
        ],
        "status": "SUCCESS"
    }


.. code-block:: python

    # 识别未完成
    {
        "task_id": "5b8cdee3d300ca0001410146",
        "status": "PENDING"
    }   

.. code-block:: python

    # 识别出错
    {
        "task_id": "5b8cdee3d300ca0001410146",
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
	        {
	            "begin_time": 0,
	            "channel_id": 0,
	            "end_time": 11950,
	            "speaker_type": "s",
	            "status": "SUCCESS",
	            "task_id": "xxxxx",
                "source_id": "",
	            "text": "喂，喂，你好，我说你儿子xxx到底还不还钱啊？"
	        },
	        ...
	    ],
	    "success": true
	}


单条语义画像获取
-----------

POST请求(json)

http://data_server.rcrai.com/{business_key}/semantic/{unique_id}

.. code-block:: python

    {
        "key": "{access_key_id}", 
        "secret":"{access_key_secret}", 
    }

.. code-block:: python

    # 成功返回结果
    {
        "entities": [
            {
                "name": "身份确认",
                "value": "身份确认", // 语义点
                "evidence": "嗯喂，你好，是是吗？喂你好， 你好，唉，你", // 语义点证据
                "briefEvidence": "",
                "mediumEvidence": "",
                "score": 0
            },
            {
                "name": "身份确认",
                "value": "身份确认",
                "evidence": "话能嗯对，堂哥 您是他堂哥是吗？喂，嗯，那你这",
                "briefEvidence": "",
                "mediumEvidence": "",
                "score": 0
            },
            ...
        ],
        "success": true // 成功
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
        "source_ids": ["id1", "id2"]  // 客户传过来的unique_id
    }

.. code-block:: python

    # 返回值:
    {
    "data": {
        "id1": {  // 与source_ids相对应
            "entities": [],
            ”source_id": xxx
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


