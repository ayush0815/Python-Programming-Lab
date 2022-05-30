#to read number of words
count = 0
f = open('info.txt','r')
for line in f:
    words = line.split()
    count += len(words)
print(count)