minute=int(input('주차시간, 분단위'))

day = minute//1440
min=minute%1440

if min>600:
    day +=1
    fee = 24000*day
elif min%1440 == 0:
    fee=day*24000
elif min<30:
    fee = day*24000+1200
else:
    additional30 = min-30#기본 30분을 뺀 추가 15분
    fee30 = additional30//15#추가 15분을 15로 나눔
    if additional30%15 !=0:
        fee30 += 1
    fee = day*24000+1200+600*fee30
    
print(fee)
