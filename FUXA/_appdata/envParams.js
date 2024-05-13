process.env.DEVICES = `[
    {
        "id":"webapi-A",
        "name":"wApi",
        "type":"WebAPI",
        "configs": {
            "getTags":"http://127.0.0.1:1888/api/tags",
            "postTags":"http://127.0.0.1:1888/api/tags",
            "requestTimeoutMs":5000,
            "requestIntervalMs":500
        }
    }
]`
;