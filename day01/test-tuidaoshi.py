
#列表推导式(list)
#names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
#
# new_name = [name.upper()for name in names if len(name)>3]
# print(new_name)

# multiples = [i for i in range(30) if i % 3 == 0]
#
# print(multiples)

#字典推导式(dict)
# listdemo = ['Google','Runoob', 'Taobao','Bob','Tom','alice','Jerry','Wendy','Smith']
#
# newdict = {key:len(key) for key in listdemo}
#
# print(newdict)
#
# dic = {x:x**2 for x in (2,4,6)}
# print(type(dic))

#集合推导式(set)
# setnew = {i**2 for i in (1,2,3)}
# print(setnew)
#
# a = {x for x in 'abracadabraqwesdf' if x not in 'abc'}
# print(a)

#元组推导式(tuple)

a = {x for x in range(1,10)}
print(a)
print(type(a))
b = tuple(a)
print(type(b))