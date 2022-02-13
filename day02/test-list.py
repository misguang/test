list = ['red', 'green', 'blue', 'yellow', 'white', 'black']

print(list[0])
print(list[-1])
print(list[0][0])
print(list[-1][0])
print(type(list[-1]))
print(type(list[-1][0]))

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]

#符合左闭右开规则
print(nums[0:4])



list = ['Google', 'Runoob', 1997, 2000]

print("原始列表 : ", list)
del list[2]
print("删除第三个元素 : ", list)


squares = [1,4,9,16,25]
print(squares)
squares += [36,49,64,81,100]
print(squares)


a= ['a','b','c']
n=[1,2,3]

x=[a,n]
print(x)

print(x[0][1])



tup1 = (50,)
print(tup1)