entry = []
entry_temp = []
dic_of_house = {}
with open('input.txt', 'r+') as f:
    for line in f.readlines():
        entry_temp.append(line)
for i in entry_temp:
    entry.append(i.strip())

string_nice = 0
lEntry = len(entry[0])
vowels = ["a","e","i","o","u"]
str_non = ["ab","cd","pq","xy"]

for sEntry in entry:
    cmp_string_nice = False
    count_vowels = 0#this is for 1
    for sub in sEntry:
        if sub in vowels:
            count_vowels += 1
        if(count_vowels>=3):
            cmp_string_nice = True
            break

    if not cmp_string_nice:
        continue
    cmp_string_nice = False
    i = 0
    while i < (lEntry-1):#This is for 2
        if sEntry[i] == sEntry[i+1]:
            cmp_string_nice = True
            break
        i += 1
    if not cmp_string_nice:
        continue
    cmp_string_nice = True
    i = 0
    while i < (lEntry-1):#This is for 3
        if (sEntry[i]+sEntry[i+1]) in str_non:
            cmp_string_nice = False
            break
        i += 1
    if not cmp_string_nice:
        continue
    string_nice +=1
print(string_nice)

#######################################################################################

string_nice = 0
for sEntry in entry:
    first = False
    for i in range(lEntry - 3):
        sub = sEntry[i: i + 2]
        if sub in sEntry[i + 2:]:
            first = True
            break
    if not first:
        continue
    second = False
    for i in range(lEntry - 2):
        if sEntry[i] == sEntry[i + 2]:
            second = True
            break
    if not second:
        continue
    string_nice +=1
print(string_nice)
