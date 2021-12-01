import requests
import random
import threading
import os

os.system('cls' if os.name == 'nt' else 'clear')

banner=("""\n\n
____    __    ____  __  ___   ___ .___________.
\   \  /  \  /   / |  | \  \ /  / |           |
 \   \/    \/   /  |  |  \  V  /  `---|  |----`
  \            /   |  |   >   <       |  |     
   \    /\    /    |  |  /  .  \      |  |     
    \__/  \__/     |__| /__/ \__\     |__|     
                                               
\n""")
print(banner)

def DL_PROXY():
    DL = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=yes")
    with open("proxies.txt","wb") as WP:
        WP.write(DL.content)
def RD_PROXY():
    with open("proxies.txt","r") as R:
        RL = R.readlines()
    RD = random.choice(RL)
    RD = f"https://{RD}".strip("\n")
    return RD
def FINDER():
    try:
        while True:
            ID = random.randint(1300000,7300000)
            PXYDIC = {
            "https": RD_PROXY()
            }
            REQ = requests.get(f"https://groups.roblox.com/v1/groups/{ID}",proxies=PXYDIC,verify=True,timeout=5)
            REQJSN = REQ.json()
            if REQ.status_code == 200 and REQJSN["owner"] == None and REQJSN["publicEntryAllowed"] == True and REQJSN["isLocked"] == False:
                DC = requests.post(webhook,data={"content": f"https://www.roblox.com/groups/{ID}"})
            else:
                print(f"{REQ.status_code} | {REQJSN['id']} | {REQJSN['name']}")
    except:
        pass
def START():
    while True:
        for i in range(10):
            thread = threading.Thread(target=FINDER)
            thread.start()
webhook = input("Webhook URL >> ")
dl_proxy = input("Download Proxy List? >> ")
webhook_check = requests.get(webhook)
if dl_proxy == "y":
    DL_PROXY()
elif dl_proxy == "n":
    None
else:
    DL_PROXY()
if webhook_check.status_code == 401:
    print(f"{webhook_check.status_code}")
elif webhook_check.status_code == 200:
    START()
else:
    print(f"{webhook_check.status_code}")
os.system('cls' if os.name == 'nt' else 'clear')