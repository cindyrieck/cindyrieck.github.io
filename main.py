import requests
import threading
import time
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

owner = [1029308249935183902,627401573529681921]

user_list = []
my_file1 = open("username.txt","r")
idlist1 = my_file1.readlines()
for id1 in idlist1:
    id = id1.replace("\n","")
    user_list.append(id)

def userlogin(username, password):
    url = "https://api.tsuprod.com/api/v1/user/login"
    head = {
        "Host": "api.tsuprod.com",
        "x-api-key": "Lb1GVRNi6Qh1Mk7QXOTq9hVMES5pBzi7IiN0Yhw2",
        "app_version": "2.4.5.2",
        "version_code": "154",
        "device_model": "realme RMX3081",
        "device_os": "Android",
        "device_os_version": "30",
        "content-type": "application/json; charset=UTF-8",
        "content-length": "123",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/4.9.1"
    }
    data = {"login":username,"password":password,"client_version":"2.4.0.3(154)","device_id":"android","device_type":"android"}
    r = requests.post(url, headers=head, json=data)
    n = r.json()
    id = n["data"]["id"]
    token = n["data"]["auth_token"]
    return id,token

def login(username):
    url = "https://api.tsuprod.com/api/v1/user/login"
    head = {
        "Host": "api.tsuprod.com",
        "x-api-key": "Lb1GVRNi6Qh1Mk7QXOTq9hVMES5pBzi7IiN0Yhw2",
        "app_version": "2.4.5.2",
        "version_code": "154",
        "device_model": "realme RMX3081",
        "device_os": "Android",
        "device_os_version": "30",
        "content-type": "application/json; charset=UTF-8",
        "content-length": "123",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/4.9.1"
    }
    data = {"login":username,"password":"Myran@123","client_version":"2.4.0.3(154)","device_id":"android","device_type":"android"}
    r = requests.post(url, headers=head, json=data)
    n = r.json()
    id = n["data"]["id"]
    token = n["data"]["auth_token"]
    return id,token

def follow1(id, token, cu):
    url = f"https://api.tsuprod.com/api/v1/friends/{id}/follow"
    head = {
    "Host": "api.tsuprod.com",
    "x-api-key": "Lb1GVRNi6Qh1Mk7QXOTq9hVMES5pBzi7IiN0Yhw2",
    "app_version": "2.4.4.2",
    "version_code": "170",
    "device_model": "motorola Moto G (5S) Plus",
    "device_os": "Android",
    "device_os_version": "27",
    "authorization": f"Bearer {token}",
    "access_token": f"{token}",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.9.3"
    }
    try:
        r = requests.get(url, headers=head)
        if r.status_code == 200:
            print(cu, "success")
    except:
        time.sleep(60)
        pass

@bot.command()
async def follow(ctx, login1, password):
    if ctx.author.id in owner:
        embed = discord.Embed(description="Checking ...",color=0x00ff00)
        x = await ctx.send(embed=embed)
        lp = userlogin(login1, password)
        cu = 0
        for name in user_list:
            cu += 1
            data = login(name)
            threading.Thread(target=follow1, args=(lp[0], data[1], cu)).start()
            embed1 = discord.Embed(description=f"{cu} follow to your account",color=0x00ff00)
            await x.edit(embed=embed1)
    else:
        await ctx.send("Check Owner 🤣")

def detail(id, token):
    url = f"https://api.tsuprod.com/api/v1/posts/list/{id}?count=10"
    head = {
    "Host": "api.tsuprod.com",
    "x-api-key": "Lb1GVRNi6Qh1Mk7QXOTq9hVMES5pBzi7IiN0Yhw2",
    "app_version": "2.4.4.2",
    "version_code": "170",
    "device_model": "motorola Moto G (5S) Plus",
    "device_os": "Android",
    "device_os_version": "27",
    "authorization": f"Bearer {token}",
    "access_token": f"{token}",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.9.3"
    }
    r = requests.get(url, headers=head)
    id = (r.json()["data"]["posts"][0]["id"])
    return id


def postlike(id, token):
    url = f"https://api.tsuprod.com/api/v1/posts/{id}/like"
    head = {
    "Host": "api.tsuprod.com",
    "x-api-key": "Lb1GVRNi6Qh1Mk7QXOTq9hVMES5pBzi7IiN0Yhw2",
    "app_version": "2.4.4.2",
    "version_code": "170",
    "device_model": "motorola Moto G (5S) Plus",
    "device_os": "Android",
    "device_os_version": "27",
    "authorization": f"Bearer {token}",
    "access_token": f"{token}",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.9.3"
    }
    requests.put(url, headers=head)

def postsupport(id, token):
    url = f"https://api.tsuprod.com/api/v2/posts/{id}/support"
    head = {
    "Host": "api.tsuprod.com",
    "x-api-key": "Lb1GVRNi6Qh1Mk7QXOTq9hVMES5pBzi7IiN0Yhw2",
    "app_version": "2.4.4.2",
    "version_code": "170",
    "device_model": "motorola Moto G (5S) Plus",
    "device_os": "Android",
    "device_os_version": "27",
    "authorization": f"Bearer {token}",
    "access_token": f"{token}",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.9.3"
    }
    requests.post(url, headers=head)

def postcomment(id, token):
    url = f"https://api.tsuprod.com/api/comments/{id}"
    head = {
    "Host": "api.tsuprod.com",
    "x-api-key": "Lb1GVRNi6Qh1Mk7QXOTq9hVMES5pBzi7IiN0Yhw2",
    "app_version": "2.4.4.2",
    "version_code": "170",
    "device_model": "motorola Moto G (5S) Plus",
    "device_os": "Android",
    "device_os_version": "27",
    "authorization": f"Bearer {token}",
    "access_token": f"{token}",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.9.3"
    }
    data = {"text":"i like your every posts"}
    r = requests.post(url, headers=head, json=data)
    if r.status_code != 200:
        print("error",r.text)

@bot.command()
async def start(ctx, login1, password):
    if ctx.author.id in owner:
        embed = discord.Embed(description="Checking ...",color=0x00ff00)
        x = await ctx.send(embed=embed)
        lp = userlogin(login1, password)
        pid = detail(lp[0],lp[1])
        cu = 0
        for name in user_list:
            cu += 1
            data = login(name)
            threading.Thread(target=postlike, args=(pid, data[1])).start()
            threading.Thread(target=postcomment, args=(pid, data[1])).start()
            threading.Thread(target=postsupport, args=(pid, data[1])).start()
            embed1 = discord.Embed(description=f"{cu} users have been supported",color=0x00ff00)
            await x.edit(embed=embed1)
    else:
        await ctx.send("Check Owner 🤣")

bot.run("MTAzMDg1OTE5MTU3OTA1ODE5Ng.GHUR3B.mvGOzZswToR3KpnW0VcoaN6aTJ8XnUXt2ZHeD4")
