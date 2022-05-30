#to return the longest line
f = open('info.txt','r')
data = f.readlines()
out = len(max(data, key = len))
for i in data:
    if len(i) == out:
        print(i)
f.close()