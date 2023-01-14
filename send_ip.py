import time
import requests
import subprocess
from datetime import datetime
from config import BOT_TOKEN, BOT_CHATID

def sendIp(hostname : str, ip : str):
    now = datetime.now()
    API_HEADER = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + BOT_CHATID + '&parse_mode=Markdown&text='
    msg = API_HEADER + f'Raspberry Pi {hostname} alive!\nIP: {ip}\n' + f'Date: {now.strftime("%d/%m/%Y %H:%M:%S")}'
    response = requests.get(msg)

    return response.json()

def getIp():
    return subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip('\n')

ip = getIp()
while not ip:
    ip=getIp()
hostname = subprocess.run(['hostname'], stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip('\n')
sent = False
while not sent:
    try:
        sendIp(hostname, ip)
        sent = True
    except:
        time.sleep(2)
        continue
