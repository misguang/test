tinydict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
emptyDict = {}

print(emptyDict)
print(len(emptyDict))
print(type(emptyDict))

print(len(tinydict))
print(tinydict)
print(type(tinydict))

# Get Dict values
tinydict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("tinydict1['Name']: ", tinydict1['Name'])
print("tinydict1['Age']: ", tinydict1['Age'])

# print('sorce: ', tinydict1['sorce'] )

# dict Update & Add
tinydict1['Age'] = 9
tinydict1['School'] = '菜鸟教程'

print(tinydict1)

# delete dict
tinydict2 = {'Name': 'Runoob', 'Age': 9, 'Class': 'First', 'School': '菜鸟教程'}

del tinydict2['Name']   #删除键
#print(tinydict2['Name'])   #执行后报错：KeyError: 'Name'
tinydict2.clear()   #执行后清空字典
print(tinydict2)
del tinydict    #删除字典
print(tinydict) #删除后报错：NameError: name 'tinydict' is not defined
