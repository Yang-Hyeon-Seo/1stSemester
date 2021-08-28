sec=int(input('초를 입력하세요'))
min = sec//60
hour = min//60
minute = min%60
sec_ = sec%60
print('%d시간 %d분 %d 초'%(hour, minute, sec_))
