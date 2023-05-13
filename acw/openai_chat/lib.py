import requests
import os
import time
import json
from . import config
def main(obj):
            o=main1(obj)
            return json.dumps(o)

os.makedirs(config.path_log+'/responses/',exist_ok=True)
os.makedirs(config.path_log+'/prompts/',exist_ok=True)

def main1(o):
    i_log=int(time.time()*10)
    with open(config.path_log+f'/prompts/{i_log}.json','w') as f:
        json.dump(o,f,indent='  ',ensure_ascii=False)

    assert o['deployment_id'] is None 

    headers = {"Authorization": "Bearer " + config.key, "Content-Type": "application/json"}
    proxies = {'http': config.proxy, 'https': config.proxy}
    u = 'https://api.openai.com/v1/chat/completions'
    data = {"model": o['model'], "messages": o['messages'], "temperature": o['temperature'],"max_tokens":o["max_tokens"]}
    while True:
        #基本上这里都是手操，所以完全可以try except
        try:
            r = requests.post(u, json.dumps(data), headers=headers, proxies=proxies)
            o = r.json()
            if 'error' in o:
                print(o['error']['message'])
                if 'Rate limit reached' in o['error']['message']:
                    time.sleep(20) #限制似乎是20秒
                    continue
            break
        except:
            print('connection error')
            time.sleep(1)
            pass
    with open(config.path_log+f'/responses/{i_log}.json','w') as f:
        json.dump(o,f,indent='  ',ensure_ascii=False)
    return o
#    choi=o['choices']
#    x = json.loads(r.content, object_hook=lambda d: SimpleNamespace(**d))
#    for i in range(len(x.choices)):
#        #在openai的api中，这部份依然是json，而不是obj
#        x.choices[i].message=choi[i]['message']
#    return x
