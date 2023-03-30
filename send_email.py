import smtplib


def send_mail(urls):
    # 设置发件人和收件人
    sender = '2797037795@qq.com'
    recipient = 'c15871258342@163.com'

    # 配置 SMTP 服务器
    smtp_server = 'smtp.qq.com'
    smtp_port = 587

    # 连接到 SMTP 服务器
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()

    # 输入发件人邮箱和密码进行登录
    username = '2797037795@qq.com'
    password = password
    server.login(username, password)

    # 发送邮件
    message = 'Subject: your website has updated!\n\n{} updated'.format(urls)
    server.sendmail(sender, recipient, message)

    # 断开连接
    server.quit()


if __name__ == '__main__':
    url = "www.baidu.com"
    send_mail(url)
