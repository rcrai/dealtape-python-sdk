Recurrent.ai DealTape REST API
====================================

数据推送:
-------


POST请求(json)
http://data_server.rcrai.com/{business_key}/call/


-------------
.. code-block:: python

    {
        "unique_id": "133333333",  // 电话在客户内部系统中的唯一标识
        "url":"http://voice-2.cticloud.cn/05062017/record/7000001/7000001-20170605192458-15302529829-02145994742--record-sip-1-1496661898.303292.mp3", // 电话录音的url
        "timestamp":1484640092, 电话的拨打时间(UNIX时间戳，中国时间)
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
            }
        },
        "customer":{
            "id": "1345" // 客户的唯一标识
            "phone":"xxxxxxx5229",  // 客户电话号码
            "name":"李四",  // 客户的名称
        }
    }


语义画像获取
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
                "id": "5b73e94935842e0b838ad318",
                "bid": "599d1ff844ff53119a13e545",
                "sid": "",
                "cid": "5aefccf02aa1d4001331fdc5",
                "uniqueId": "",
                "name": "身份确认",
                "value": "身份确认", // 语义点
                "evidence": "嗯喂，你好，是是吗？喂你好， 你好，唉，你", // 语义点证据
                "briefEvidence": "",
                "mediumEvidence": "",
                "score": 0
            },
            {
                "id": "5b73e94935842e0b838ad319",
                "bid": "599d1ff844ff53119a13e545",
                "sid": "",
                "cid": "5aefccf02aa1d4001331fdc5",
                "uniqueId": "",
                "name": "身份确认",
                "value": "身份确认",
                "evidence": "话能嗯对，堂哥 您是他堂哥是吗？喂，嗯，那你这",
                "briefEvidence": "",
                "mediumEvidence": "",
                "score": 0
            },
            {
                "id": "5b73e94935842e0b838ad31a",
                "bid": "599d1ff844ff53119a13e545",
                "sid": "",
                "cid": "5aefccf02aa1d4001331fdc5",
                "uniqueId": "",
                "name": "自我介绍",
                "value": "自我介绍",
                "evidence": "？你是怎么弄啊，我这块是捷信法务部的，捷信委托的法",
                "briefEvidence": "",
                "mediumEvidence": "",
                "score": 0
            },
            {
                "id": "5b73e94935842e0b838ad31c",
                "bid": "599d1ff844ff53119a13e545",
                "sid": "",
                "cid": "5aefccf02aa1d4001331fdc5",
                "uniqueId": "",
                "name": "描述借款信息",
                "value": "描述借款信息",
                "evidence": "，你这块是是已经逾期了120天一千的，然后你直",
                "briefEvidence": "",
                "mediumEvidence": "",
                "score": 0
            },
            {
                "id": "5b73e94935842e0b838ad31d",
                "bid": "599d1ff844ff53119a13e545",
                "sid": "",
                "cid": "5aefccf02aa1d4001331fdc5",
                "uniqueId": "",
                "name": "描述借款信息",
                "value": "描述借款信息",
                "evidence": "上的话，你看已经逾期81天了，并不是说一两",
                "briefEvidence": "",
                "mediumEvidence": "",
                "score": 0
            },
            {
                "id": "5b73e94935842e0b838ad31f",
                "bid": "599d1ff844ff53119a13e545",
                "sid": "",
                "cid": "5aefccf02aa1d4001331fdc5",
                "uniqueId": "",
                "name": "协商转告",
                "value": "协商转告",
                "evidence": "我一下吗？我电话联系他本人好吗，我加下你的",
                "briefEvidence": "",
                "mediumEvidence": "",
                "score": 0
            },
            {
                "id": "5b73e94935842e0b838ad320",
                "bid": "599d1ff844ff53119a13e545",
                "sid": "",
                "cid": "5aefccf02aa1d4001331fdc5",
                "uniqueId": "",
                "name": "协商转告",
                "value": "协商转告",
                "evidence": "是我们的，还需要联系上他本人，这一块的话，大",
                "briefEvidence": "",
                "mediumEvidence": "",
                "score": 0
            },
            {
                "id": "5b73e94935842e0b838ad321",
                "bid": "599d1ff844ff53119a13e545",
                "sid": "",
                "cid": "5aefccf02aa1d4001331fdc5",
                "uniqueId": "",
                "name": "协商转告",
                "value": "协商转告",
                "evidence": "嗯，那你这个不能联系到本人把他本人号码给我",
                "briefEvidence": "",
                "mediumEvidence": "",
                "score": 0
            },
            {
                "id": "5b73e94935842e0b838ad32d",
                "bid": "599d1ff844ff53119a13e545",
                "sid": "",
                "cid": "5aefccf02aa1d4001331fdc5",
                "uniqueId": "",
                "name": "协商还款",
                "value": "协商还款",
                "evidence": "你直说不还了，是什么时候还呢，这个这个这个",
                "briefEvidence": "",
                "mediumEvidence": "",
                "score": 0
            },
            {
                "id": "5b73e94935842e0b838ad32f",
                "bid": "599d1ff844ff53119a13e545",
                "sid": "",
                "cid": "5aefccf02aa1d4001331fdc5",
                "uniqueId": "",
                "name": "协商还款",
                "value": "协商还款",
                "evidence": "快的明天这个6点之前处理一下这个款了，如",
                "briefEvidence": "",
                "mediumEvidence": "",
                "score": 0
            },
            {
                "id": "5b73e94935842e0b838ad330",
                "bid": "599d1ff844ff53119a13e545",
                "sid": "",
                "cid": "5aefccf02aa1d4001331fdc5",
                "uniqueId": "",
                "name": "法律施压",
                "value": "法律施压",
                "evidence": "我们可能会涉及到法律问题 期，也就是说在",
                "briefEvidence": "",
                "mediumEvidence": "",
                "score": 0
            },
            {
                "id": "5b73e94935842e0b838ad333",
                "bid": "599d1ff844ff53119a13e545",
                "sid": "",
                "cid": "5aefccf02aa1d4001331fdc5",
                "uniqueId": "",
                "name": "信用施压",
                "value": "信用施压",
                "evidence": "话，涉及到以后的征信 征信问题，他跟",
                "briefEvidence": "",
                "mediumEvidence": "",
                "score": 0
            },
            {
                "id": "5b73e94935842e0b838ad334",
                "bid": "599d1ff844ff53119a13e545",
                "sid": "",
                "cid": "5aefccf02aa1d4001331fdc5",
                "uniqueId": "",
                "name": "生活限制",
                "value": "生活限制",
                "evidence": "个信用卡问题或者上学问题 包括在往后延伸",
                "briefEvidence": "",
                "mediumEvidence": "",
                "score": 0
            },
            {
                "id": "5b73e94935842e0b838ad335",
                "bid": "599d1ff844ff53119a13e545",
                "sid": "",
                "cid": "5aefccf02aa1d4001331fdc5",
                "uniqueId": "",
                "name": "确认还款",
                "value": "确认还款",
                "evidence": "再给你打电话，4点多给我打电话，到时 嗯，这样子，我",
                "briefEvidence": "",
                "mediumEvidence": "",
                "score": 0
            }
        ],
        "success": true // 成功
    }


