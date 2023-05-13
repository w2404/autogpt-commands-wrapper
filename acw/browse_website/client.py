
import requests
import json
def sendcmd(obj):
    return requests.post('http://localhost:12712',json.dumps(obj).encode()).json()
sendcmd({'command':'get','url':'http://baidu.com'})
sendcmd({'command':'page_source'})


