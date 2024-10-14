'''
You will need to create your own webhook to replace the URL below.
1. own a discord server
2. go to server settings
3. look under APPS>Integrations
4. click on Webhooks
5. click on the New Webhook button
6. click on new webhook and give it a new name, assign a default channel, and finally:
7. click Copy Webhook URL button

obvioulsy, requires the discord lib for python. install with ''pip install discord''.
'''
import sys
from discord import Webhook, RequestsWebhookAdapter

def send ( message):
    webhook = Webhook.from_url("https://YOUR.WEBHOOK.URL/HERE", adapter=RequestsWebhookAdapter())
    webhook.send(message)

send( sys.argv[1] )
