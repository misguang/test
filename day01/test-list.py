
#列表推导式
#names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
#
# new_name = [name.upper()for name in names if len(name)>3]
# print(new_name)

# multiples = [i for i in range(30) if i % 3 == 0]
#
# print(multiples)

#字典推导式
listdemo = ['Google','Runoob', 'Taobao','Bob','Tom','alice','Jerry','Wendy','Smith']

newdict = {key:len(key) for key in listdemo}

print(newdict)