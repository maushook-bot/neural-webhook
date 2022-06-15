import requests
import json


webhook_url = 'http://127.0.0.1:7500/webhook'

data = {
    'message': "Hi I'm a webhook",
    'webhook url': webhook_url
}

r = requests.post(webhook_url,
                  data=json.dumps(data),
                  headers={'Content-Type': 'application/json'},
                  )