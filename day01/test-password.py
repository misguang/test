a = input("请输入你的密码：")
b = a.isdigit()
print(b)
while b != True:
    c = input("密码不符合，请重新输入密码：")
    b = a.isdigit()
    passwd = c
else:
    passwd = a

print(passwd)
