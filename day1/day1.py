x = ""
with open('input.txt', 'r+') as f:
    for line in f.readlines():
        x = line

floor = 0

for i in x:
    if i =="(":
        floor = floor + 1
    else:
        floor = floor - 1

print(floor)

floor = 0
cnt = 0
for i in x:
    cnt = cnt + 1
    if i =="(":
        floor = floor + 1
    else:
        floor = floor - 1
    if floor == -1:
        break
print(cnt)