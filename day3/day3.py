entry = []
entry_temp = []
dic_of_house = {}
with open('input.txt', 'r+') as f:
    for line in f.readlines():
        entry_temp.append(line)
for i in entry_temp:
    entry.append(i.strip())
xs, ys = 0,0
xr, yr = 0,0
lEntry = len(entry[0])
i = 0
var_to_dic = "xs" +"-"+ "ys"
dic_of_house[var_to_dic] = 1

while i < lEntry:
    if entry[0][i] == ">":
        xs += 1
    elif entry[0][i] == "<":
        xs -= 1
    elif entry[0][i] == "^":
        ys += 1
    elif entry[0][i] == "v":
        ys -= 1
    var_to_dic = str(xs) +"-"+ str(ys)
    dic_of_house[var_to_dic] = 1
    i += 1

print(len(dic_of_house))

dic_of_house.clear()
xs = 0
ys = 0
i = 0

var_to_dic = "0" +"-"+ "0"
dic_of_house[var_to_dic] = 1

while i < lEntry:
    if i%2 == 0:
        if entry[0][i] == ">":
            xs += 1
        elif entry[0][i] == "<":
            xs -= 1
        elif entry[0][i] == "^":
            ys += 1
        elif entry[0][i] == "v":
            ys -= 1
        var_to_dic = str(xs) +"-"+ str(ys)
    else:
        if entry[0][i] == ">":
            xr += 1
        elif entry[0][i] == "<":
            xr -= 1
        elif entry[0][i] == "^":
            yr += 1
        elif entry[0][i] == "v":
            yr -= 1
        var_to_dic = str(xr) +"-"+ str(yr)
    dic_of_house[ var_to_dic ] = 1
    i += 1
print(len(dic_of_house))
