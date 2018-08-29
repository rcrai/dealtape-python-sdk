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

    client = DealTapeClient(business=business, access_key_id=access_key_id, access_key_secret=access_key_secret)



数据推送
--------
.. code-block:: python

    item = CallLog(
        url="CALLLOG_AUDIO_URL", # 电话录音的url
        id="CALLLOG_UNIQUE_IDENTIFIER", # 电话在客户内部系统中的唯一标识
        staff_id="STAFF_ID", # 该电话坐席的唯一标识
        staff_name="STAFF_NAME", # 该电话坐席名称
        customer_id="CUSTOMER_ID", # 客户的唯一标识
        customer_id="CUSTOMER_NAME", # 客户的名称
        deal_closed=True/False/None, # 该电话是否成单
        timestamp=TIMESTAMP # 电话的拨打时间（datetime.datetime类型, 或是int类型的unix时间戳）
    )
    resp = client.push_calllog(item)
    if not resp.ok:
        print(resp.text)


语音识别结果获取
-------------

.. code-block:: python

    resp = client.get_transcript(source_id=CALLLOG_UNIQUE_IDENTIFIER) # 电话在客户内部系统中的唯一标识
    if not resp.ok:
        print(resp.text)


语义画像获取
-------------

.. code-block:: python

    resp = client.get_semantic(source_id=CALLLOG_UNIQUE_IDENTIFIER) # 电话在客户内部系统中的唯一标识
    if not resp.ok:
        print(resp.text)

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
