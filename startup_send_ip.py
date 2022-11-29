import time
import requests
import subprocess
from datetime import datetime
from config import BOT_TOKEN, BOT_CHATID

def sendText(msg):
    now = datetime.now()
    send_text = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + BOT_CHATID + '&parse_mode=Markdown&text=' + f'Raspberry Pi IP: {msg}\n' + f'Date: {now.strftime("%d/%m/%Y %H:%M:%S")}'

    response = requests.get(send_text)

    return response.json()

res = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE)
res = res.stdout.decode('utf-8')
sent = False
while not sent:
    try:
        sendText(res)
        sent = True
    except:
        time.sleep(2)
        continue