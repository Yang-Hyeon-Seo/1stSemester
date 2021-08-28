import time

upper=1000

def prime1 ():
    global upper
    num=[]
    t1=time.time()
    for i in range(2,upper+1):
        prime = True
        if i == 2:
            pass
        else:
            for j in range(2,i):
                if i%j ==0:
                    prime=False
                    break
        if prime == True:
            num.append(i)
    t2=time.time()
    print('걸린 시간 :',t2-t1)
    print('소수', num)
    print(len(num),'개')

prime1()

