entry = []
entry_temp = []
with open('input.txt', 'r+') as f:
    for line in f.readlines():
        entry_temp.append(line)
for i in entry_temp:
    entry.append(i.strip())
totalPaper = 0
totalRibbon = 0
#print(entry)
#l   w   h
#2   3   4
#l = x[0] ||| w = x[1] ||| h = x[2]
def calcMin(l,w,h):
    if(l<=h and w<=h):
        return l,w
    elif(l<=w and h<=w):
        return l,h
    elif(w<=l and h<=l):
        return w,h
    return 0,0

for x in entry:
    x = x.split('x')
    l = int(x[0])
    w = int(x[1])
    h = int(x[2])
    min1,min2 = calcMin(l,w,h)
    totalPaper += (2*l*w + 2*w*h + 2*h*l) + min1*min2
    totalRibbon += (l*w*h) + (2*min1+2*min2)

print(totalPaper)

print(totalRibbon)
