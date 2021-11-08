import json
import requests
from pandas.io.json import json_normalize

slack_token = 'xoxb-2637151350448-2663729429670-CLAM6RcUv7FxjarHDyYaS63z'
# 파라미터
data = {'Content-Type': 'application/x-www-form-urlencoded',
        'token': slack_token,
        'channel': 'test',
        'text': 'testtttt',
        }

# 메시지 등록 API 메소드: chat.postMessage
URL = "https://slack.com/api/chat.postMessage"
res = requests.post(URL, data=data)
