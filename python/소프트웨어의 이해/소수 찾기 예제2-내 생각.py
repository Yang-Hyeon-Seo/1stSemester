import time

t1=time.time()
num=[]
for n in range(2, 1000):
    num.append(n)
for i in num:
    for j in range(2,1000):
        s=i*j
        if s > 1000:
            break
        if s in num:
            num.remove(s)
t2=time.time()

print(t2-t1,'초')
print(num)
print(len(num),'개')
