str = 'Hello World!'

s = {a for a in str if a not in 'elo'}

print(s)

i = {k for k in range(0,len(str))}
print(i)
