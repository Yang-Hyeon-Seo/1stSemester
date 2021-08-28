

#
unpper_num=100
numbers=[]

for i in range(2,101):
    if i<upper_num:
    for m in range(2,101):
        for n in range(2,101):
            if i != m*n:
                 numbers.append(i)
