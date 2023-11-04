def create_notification(data,student_name1):

    notifications0 = []  # 通知列表
    # notifications1 = []  # 通知列表
    # notifications2 = []  # 通知列表
    #column = data['姓名']
    #print(column)
    text="亲爱的["+student_name1+"]同学:\n祝贺您顺利完成本学期的学习！教务处在此向您发送最新的成绩单。"

    for index, row in data.iterrows():
        student_name = row['姓名']
        student_id = row['学号']
        grade = row['百分成绩']
        subject = row['课程名称']
        #notification = f'姓名：{student_name}\n学号：{student_id}\n成绩：{grade}\n课程名称:{subject}\n'

        if student_name ==student_name1:
            text=text+'['+subject+']'+ '：['+str(grade)+']\n'
        # elif student_name == '李四':
        #     notifications1.append({'name': student_name, 'notification': notification})
        # elif student_name == '王五':
        #     notifications2.append({'name': student_name, 'notification': notification})
        
    text=text+'希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。再次恭喜您，祝您学习进步、事业成功！教务处'
    return text
