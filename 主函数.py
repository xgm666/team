def main():
    file_path = "grade.xlsx" 
    data = import_excel(file_path)
    namelist=[]

    for index,row in data.iterrows():
        student_name = row['姓名']
        if index == 0:
            namelist.append(student_name)
            continue
        flag=1
        for row2 in namelist:
            if student_name == row2:
                flag=0
                #print(1)
        if(flag==1 and index!=1):
            namelist.append(student_name)
    for row3 in namelist:
        text = create_notification(data,row3)
         # 设置邮箱服务器和登录信息
        print(text)
