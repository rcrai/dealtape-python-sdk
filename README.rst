Recurrent.ai DealTape SDK for Python
====================================


概述
--------

DealTape数据SDK


安装方式
--------

使用PIP进行安装（以Linux系统为例）

.. code-block:: bash
    
    $ pip install dealtape

也可以直接安装解压后的安装包

.. code-block:: bash

    $ sudo python setup.py install


快速使用
-------
.. code-block:: python

    # -*- coding: utf-8 -*-
    from dealtape import CallLog, DealTapeClient

    business = 'YOUR_BUSINESS_KEY' # 企业的唯一标识，即在企业DealTape系统中的二级域名

    client = DealTapeClient(business=business)



数据推送
--------
.. code-block:: python

    # -*- coding: utf-8 -*-
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