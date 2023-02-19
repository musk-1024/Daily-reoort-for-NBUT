import json
import requests
import time
import random
import os
import NoticePush
import markdown
import GlobalVariable

def time_random():
    start = int(round(time.time() * 1000))
    # t = random.randint(0, 1) #测试用
    t = random.randint(0, 3600000)  # 在一小时内随机取出
    end = start + t
    print(end)
    return end,t

def report(stamp_random):
    headers={'Host': 'form.nbut.edu.cn',
        'Connection': 'keep-alive',
        'Content-Length': '871',
        'Access-Control-Allow-Origin': '*',
        'Accept': 'application/json, text/plain, */*',
        'Access-Control-Allow-Credentials': 'true',
        'Authentication': GlobalVariable.Authentication,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6304051b)',
        'Origin': 'https://form.nbut.edu.cn',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'JSESSIONID=BC15ED74EFE4EA3C2CA702F3C8350A53',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://form.nbut.edu.cn/&state=STATE',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'}


    if type(GlobalVariable.TEXT) == dict:
        text = repr(GlobalVariable.TEXT)
    else :
        text = GlobalVariable.TEXT
    data = eval(text.replace('stamp',str(stamp_random)).replace('date',time.strftime("%Y-%m-%d", time.localtime())).replace('month',time.strftime("%Y-%m", time.localtime())))
    # data = eval(text.replace('stamp',str(stamp_random)).replace('date',time.strftime("%Y-%m-%d", time.localtime())).replace('month',time.strftime("%Y-%m", time.localtime())).replace('last',GlobalVariable.least))
    datas=json.dumps(data)
    r=requests.post("https://form.nbut.edu.cn/dfi/formData/saveFormSubmitData", data=datas, headers=headers, verify=False)
    print(r.text)
    result = r.json()
    title = '每日健康打卡 %s'%result.get('message')
    message(title, text)

def message(title,Content):

    NoticePush.server_push(title, Content)
    NoticePush.push_plus(title, Content)
    NoticePush.Push_Deer(title,Content)
    NoticePush.telegram_bot(title, Content)
    NoticePush.bark(title, Content)
    NoticePush.enterprise_wechat(title, Content)


    # 信息输出测试
    print("标题->", title)
    # print("内容->\n", normalContent)


if __name__ == '__main__':
    stamp_random,t_random = time_random()
    tt = int(t_random / 1000)
    print(tt)
    time.sleep (tt)
    report(stamp_random)