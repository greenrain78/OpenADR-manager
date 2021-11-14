import json
import requests
from pandas.io.json import json_normalize

slack_token = 'xoxb-2637151350448-2663729429670-CXuyzwkDgjV0uXEE9zRfzeSl'
# 파라미터
data = {'Content-Type': 'application/x-www-form-urlencoded',
        'token': slack_token,
        'channel': 'test',
        'text': '정상 동작',
        }

# 메시지 등록 API 메소드: chat.postMessage
URL = "https://slack.com/api/chat.postMessage"
res = requests.post(URL, data=data)
