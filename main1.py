import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

root = tk.Tk()
file_path = ''


# 导入成绩表
def import_excel(file_path):
    data = pd.read_excel(file_path, skiprows=1)
    return data


# 生成通知
def create_notification(data, student_name1):
    text = "亲爱的[" + student_name1 + "]同学:\n祝贺您顺利完成本学期的学习！教务处在此向您发送最新的成绩单。"

    for index, row in data.iterrows():
        student_name = row['姓名']
        grade = row['百分成绩']
        subject = row['课程名称']

        if student_name == student_name1:
            text = text + '[' + subject + ']' + ':[' + str(grade) + ']\n'
    
    text = text + "希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。再次恭喜您，祝您学习进步、事业成功！\n教务处"
    return text


# 发送通知
def send_notifications(notifications, _email):
    smtp_server = "smtp.qq.com"
    smtp_port = 587
    smtp_username = "2473273950@qq.com"  # 邮件名
    smtp_password = "fenogtazvwsjdjga"  # 授权码

    # 创建SMTP客户端
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # 构建邮件
    msg = MIMEMultipart()
    msg["From"] = smtp_username
    msg["To"] = _email  # 收件人
    msg["Subject"] = "邮件主题"

    body = notifications
    msg.attach(MIMEText(body, "plain"))

    # 发送邮件
    server.sendmail(smtp_username, _email, msg.as_string())

    # 关闭SMTP客户端
    server.quit()


def import_excel_button():
    global file_path
    file_path = filedialog.askopenfilename()


def create_notification_button():
    data = import_excel(file_path)
    namelist = []

    for index, row in data.iterrows():
        student_name = row['姓名']
        if index == 0:
            namelist.append(student_name)
            continue
        flag = 1
        for row2 in namelist:
            if student_name == row2:
                flag = 0
        if flag == 1 and index != 1:
            namelist.append(student_name)
    for row3 in namelist:
        text = create_notification(data, row3)
        messagebox.showinfo(title="Notification", message=text)

def create_Onenotification_button():
    student_name0 = simpledialog.askstring("姓名输入", "请输入学生姓名: ")
    data = import_excel(file_path)
    namelist = []

    for index, row in data.iterrows():
        student_name = row['姓名']
        if index == 0:
            namelist.append(student_name)
            continue
        flag = 1
        for row2 in namelist:
            if student_name == row2:
                flag = 0
        if flag == 1 and index != 1:
            namelist.append(student_name)
    text = create_notification(data, student_name0)
    messagebox.showinfo(title="Notification", message=text)

def send_notifications_button():
    sender_email = simpledialog.askstring("邮箱输入", "请输入班主任邮箱: ")
    data = import_excel(file_path)

    namelist = []

    for index, row in data.iterrows():
        student_name = row['姓名']
        if index == 0:
            namelist.append(student_name)
            continue
        flag = 1
        for row2 in namelist:
            if student_name == row2:
                flag = 0
        if flag == 1 and index != 1:
            namelist.append(student_name)
    for row3 in namelist:
        try:
            text = create_notification(data, row3)
            send_notifications(text, sender_email)
            messagebox.showinfo(title="Success", message=f"Notification sent to {row3}")
        except Exception as e:
            messagebox.showerror(title="Error", message=str(e))

def send_Onenotifications_button():
    student_name0 = simpledialog.askstring("姓名输入", "请输入学生姓名: ")
    sender_email = simpledialog.askstring("邮箱输入", "请输入学生邮箱: ")
    data = import_excel(file_path)

    namelist = []

    for index, row in data.iterrows():
        student_name = row['姓名']
        if index == 0:
            namelist.append(student_name)
            continue
        flag = 1
        for row2 in namelist:
            if student_name == row2:
                flag = 0
        if flag == 1 and index != 1:
            namelist.append(student_name)
    try:
        text = create_notification(data, student_name0)
        send_notifications(text, sender_email)
        messagebox.showinfo(title="Success", message=f"Notification sent to {student_name0}")
    except Exception as e:
        messagebox.showerror(title="Error", message=str(e))


# 主函数
def main():
    import_button = tk.Button(root, text="导入成绩单", command=import_excel_button)
    import_button.pack()

    create_notification_button = tk.Button(root, text="生成所有学生成绩单邮件内容", command=create_notification_button)
    create_notification_button.pack()

    send_notifications_button = tk.Button(root, text="发送成绩单邮件", command=send_notifications_button)
    send_notifications_button.pack()

    root.mainloop()


if __name__ == "__main__":
    import_button = tk.Button(root, text="导入成绩单", command=import_excel_button)
    import_button.pack()

    create_notification_button = tk.Button(root, text="生成所有学生成绩单邮件内容", command=create_notification_button)
    create_notification_button.pack()

    create_Onenotification_button = tk.Button(root, text="生成单个学生成绩单邮件内容", command=create_Onenotification_button)
    create_Onenotification_button.pack()

    send_notifications_button = tk.Button(root, text="发送所有学生成绩单给班主任", command=send_notifications_button)
    send_notifications_button.pack()

    send_Onenotifications_button = tk.Button(root, text="发送成绩单给学生", command=send_Onenotifications_button)
    send_Onenotifications_button.pack()

    root.mainloop()
