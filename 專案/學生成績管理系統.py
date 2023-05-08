# 學生成績管理系統
system = ['Jacky', 80, 'Eric', 95, 'Jason', 0]

while True:
    operation = input('請輸入操作指令(A)查詢(B)新增(C)刪除(D)修改(E)停止: ').upper()

    if operation == 'A':
        name = input('請輸入要查詢的姓名: ')  # 查詢姓名
        if name not in system:
            print('查無此人')
        else:
            index = system.index(name)
            print(f'{name}成績是{system[index + 1]}分')
    elif operation == 'B':
        student_data =input('請用/去分隔學生名字和成績 (例子:Jacky/80) ')
        data = student_data.split('/')  # LIST
        system.extend(data)
        print('成績新增完畢')
        print(f'目前已登入的學生人數為{int(len(system)/2)}')
        print(system)
    elif operation == 'C':
        name = input('請輸入要刪除的姓名: ')
        index = system.index(name)
        system.pop(index)
        system.pop(index)
        print(system)
    elif operation == 'D':
        name = input('請輸入要修改的同學姓名: ')
        grade = input('請輸入要修改的同學成績: ')
        index = system.index(name)
        system[index + 1] = grade
        print(system)
    elif operation == 'E':
        print(system)
        break
    else:
        print('操作錯誤，請重新確認!')