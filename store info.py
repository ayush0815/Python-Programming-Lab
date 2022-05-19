num = int(input('enter the  number\t '))
info = {}
for i in range(num):
    roll_no = int(input('enter the roll number\t'))
    name = input('enter the name of student\t')
    d1 = {}
    d2 = {}
    for j in range(5):
         sub = input('enter subject name')
         marks = int(input('enter the marks'))
         sum += marks
         d2[sub] = marks
    d1[name] = d2
    info[roll_no]=d1    
percentage = (sum/500) * 100
print(info)
print(percentage)