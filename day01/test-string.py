
# str = 'Hello World!'
#
# s = {a for a in str if a not in 'elo'}
#
# print(s)
#
# i = {k for k in range(0,len(str))}
# print(i)

# print("\a")
#
#
# print('hello \v world')
#
# print("Hello\rWorld!")
# print('google runoob taobao\r1234')

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if ("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")



print ("我叫 %s 今年 %d 岁!" % ('小明', 10))