import json
import requests
import time
import smtplib
from email.mime.text import MIMEText

least = "2022-09-23" #最近一次核酸检测时间

def email_send(news):
    '''
    邮件发送
    :param news: 发送的消息
    :return: 
    '''
    msg_from = ''  # 发送方邮箱
    passwd = ''  # 填入发送方邮箱的授权码授权码！！！

    msg_to = ['']  # 收件人邮箱
    # msg_to = ['***@163.com','***@126.com']  # 多个收件人邮箱

    subject = "nbut健康打卡"  # 主题
    content = news  # 内容

    msg = MIMEText(content)

   
    msg['Subject'] = subject

   
    msg['From'] = msg_from

    try:
        # 通过ssl方式发送，服务器地址，端口，qq和网易的有区别，注意修改。
        s = smtplib.SMTP_SSL("smtp.example.com", 465)

        # 登录到邮箱
        s.login(msg_from, passwd)

        # 发送邮件：发送方，收件方，要发送的消息
        s.sendmail(msg_from, msg_to, msg.as_string())

        print('发送成功')
    except s.SMTPException as e:
        print(e)
    finally:
        s.quit()

def All():
    headers={'Host': 'form.nbut.edu.cn',
        'Connection': 'keep-alive',
        'Content-Length': '871',
        'Access-Control-Allow-Origin': '*',
        'Accept': 'application/json, text/plain, */*',
        'Access-Control-Allow-Credentials': 'true',
        'Authentication': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.e',
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


    text = repr({
	"formWid": "33cbf04e092b4d17aef3946f245d5cb4",
	"userId": "AM@stamp522",
	"dataMap": {
		"wid": "",
		"INPUT_KWYMPWZO": "NAME",
		"INPUT_KWYMPWZP": "COMPOSE",
		"INPUT_KWZRFKE3": "CLASS",
		"INPUT_KWZ02SZK": "",
		"INPUT_KWZ02SZL": "",
		"RADIO_KWYMPX0A": "是",
		"RADIO_KX369F35": "杭州湾校区",
		"RADIO_KX1T8ENX": "否",
		"RADIO_KX1T8ENY": "否",
		"RADIO_KWYMPX04": "绿",
		"RADIO_KWYMPWZT": "是",
		"RADIO_KWYMPWZU": "两针",
		"RADIO_KWYMPWZV": "否",
		"DATEPICKER_KWYW0UX4": "last",
		"RADIO_KWYMPWZX": "阴性",
		"LOCATION_KX7NAIQR": "浙江省宁波市慈溪市",
		"INPUT_KX14LP0P": "杭州湾汽车学院",
		"RADIO_L0IZ3481": "无",
		"INPUT_KX7NAIQS": "",
		"INPUT_KX7NAIQT": "",
		"INPUT_KWYMPWZR": "",
		"RADIO_KWYMPX03": ""
	},
	"commitDate": "date",
	"commitMonth": "month",
	"auditConfigWid": ""})
    data = eval(text.replace('stamp',str(int(time.time()))).replace('date',time.strftime("%Y-%m-%d", time.localtime())).replace('month',time.strftime("%Y-%m", time.localtime())).replace('last',least))
    datas=json.dumps(data)
    r=requests.post("https://form.nbut.edu.cn/dfi/formData/saveFormSubmitData", data=datas, headers=headers)
    news = r.text
    email_send(news)
    print(r.text)

if __name__ == '__main__':
    All()
