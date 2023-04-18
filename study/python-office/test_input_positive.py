while True:
    print('请输入年龄')
    age = input()
    try:
        age = int(age)
    except:
        print('请输入整数')
        continue
    if age < 1:
        print('请输入正整数')
        continue
    break
print(f'你输入的年龄是:{age}')
