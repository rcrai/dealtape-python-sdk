Recurrent.ai DealTape REST API
====================================

### 接口URL
http://data_server.rcrai.com/{business_key}/call/

POST请求(json)
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

