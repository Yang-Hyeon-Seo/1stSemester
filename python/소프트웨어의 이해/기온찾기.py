#특정 온도 찾기 프로그램
temps=[27.9, 29.3, 21.3, 29.9, 29.6, 32.5 ,29.7, 26.3, 31.8, 34.3, 36.0, 28.0, 24.9]

target=float(input('찾고자 하는 기온 : '))
index = 0
for t in temps:
    if target == t:
        result = True
        break
    else:
        index+=1
        result = False

if result :
    print('찾음',index+1,'일')
else:
    print('찾기 못함')




#최고기온 찾기 프로그램
temps=[27.9, 29.3, 21.3, 29.9, 29.6, 32.5]
day = 0
maxday = 0
max = -100

for t in temps:
    day += 1
    if t > max:
        maxday = day
        max=t
print('월 최고기온 %d일 %.1f도'%(maxday, max))

#특정 기온 이상인 날 찾기

temps=[]
day = 0
count = 0
target = float(input('몇도 이상인 날들을 찾고 싶으세요?'))
days={}
for t in temps:
    day +=1
    if target>t:
        days.append(day)
        count += 1

for day in days:
    print(day, '일', 
        
