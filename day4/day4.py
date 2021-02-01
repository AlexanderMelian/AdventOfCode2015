import hashlib

comparer = True
key = "yzbqklnj"
i=0
while comparer:
    newkey = key+str(i)
    x = hashlib.md5(newkey.encode())
    if(x.hexdigest()[0]=='0' and x.hexdigest()[1]=='0' and  x.hexdigest()[2]=='0' and  x.hexdigest()[3]=='0' and  x.hexdigest()[4]=='0'):
        break
    i += 1
print(i)

comparer = True
key = "yzbqklnj"
i=0
while comparer:
    newkey = key+str(i)
    x = hashlib.md5(newkey.encode())
    if(x.hexdigest()[0]=='0' and x.hexdigest()[1]=='0' and x.hexdigest()[2]=='0' and x.hexdigest()[3]=='0' and x.hexdigest()[4]=='0' and x.hexdigest()[5]=='0'):
        break
    i += 1
print(i)
