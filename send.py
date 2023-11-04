def send_notifications(notifications, _email):
        smtp_server = "smtp.qq.com"
        smtp_port = 587
        smtp_username = "2473273950@qq.com"#邮件名
        smtp_password = "fenogtazvwsjdjga"#授权码

        # 创建SMTP客户端
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # 构建邮件
        msg = MIMEMultipart()
        msg["From"] = smtp_username
        msg["To"] = _email#收件人
        msg["Subject"] = "邮件主题"

        body = notifications
        msg.attach(MIMEText(body, "plain"))

        # 发送邮件
        server.sendmail(smtp_username, _email, msg.as_string())

        # 关闭SMTP客户端
        server.quit() 