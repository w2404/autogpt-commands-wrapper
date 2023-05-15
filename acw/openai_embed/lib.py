import requests
import os
import time
import json
from . import config


def main(o):
    os.makedirs(config.path_log+'/em-responses/',exist_ok=True)
    os.makedirs(config.path_log+'/em-prompts/',exist_ok=True)

    i_log=int(time.time()*10)
    with open(config.path_log+f'/em-prompts/{i_log}.json','w') as f:
        json.dump(o,f,indent='  ',ensure_ascii=False)

    headers = {"Authorization": "Bearer " + config.key, "Content-Type": "application/json"}
    proxies = {'http': config.proxy, 'https': config.proxy}
    u = 'https://api.openai.com/v1/embeddings'
    data = {"model": o['model'], "input": o['input'], }
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
    with open(config.path_log+f'/em-responses/{i_log}.json','w') as f:
        json.dump(o,f,indent='  ',ensure_ascii=False)
    return config.path_log+f'/em-responses/{i_log}.json'
    #return o
#    choi=o['choices']
#    x = json.loads(r.content, object_hook=lambda d: SimpleNamespace(**d))
#    for i in range(len(x.choices)):
#        #在openai的api中，这部份依然是json，而不是obj
#        x.choices[i].message=choi[i]['message']
#    return x
