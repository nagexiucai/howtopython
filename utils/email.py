#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/4/25 16:20
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 演示Python发送邮件（实践中需要自己搭建服务器、服务商都会有垃圾邮件检测机制）。

import smtplib
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText


SERVER = "smtp.qq.com"
PORT = 465
PASSWORD = ""
FROM = "nagexiucai@qq.com"
TO = "me@nagexiucai.com"
MSG = u'''
<html>
<head>
<meta charset="utf-8">
<title>那个秀才</title>
</head>
<body>
<a href="http://ai.nagexiucai.com/machine-learning.html">机器学习基础</a>
<hr/>
<a href="http://www.nagexiucai.com/">那个秀才</a>
<br/>
<a href="http://www.mypython.cn/">Make Young Python</a>
</body>
</html>'''

msg = MIMEText(MSG, "html", "utf-8")
msg["From"] = Header("nagexiucai.com", "utf-8")
msg["To"] = Header("pythoners", "utf-8")
msg["Subject"] = Header(u"机器学习基础——那个秀才", "utf-8").encode()

server = smtplib.SMTP_SSL(SERVER, PORT)
server.login(FROM, PASSWORD)
server.sendmail(FROM, [TO], msg.as_string())
server.quit()