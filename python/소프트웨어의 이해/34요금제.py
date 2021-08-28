기본요금 = 37400#기본요금, 음성120, 문자200, 데이터 800기본


user_voice = int(input('음성 통화시간(초) : '))
user_msg = int(input('문자건수 : '))
user_data = int(input('데이터 사용량(MB) : '))

if user_voice >120*60:
    additional_voice = user_voice - 120*60
else:
    additional_voice = 0
    
if user_msg > 200:
    additional_msg = user_msg -200
else:
    additional_msg = 0

if user_data > 800:
    additional_data = user_data-800
else:
    additional_data = 0

fee=기본요금 + additional_voice*1.98+additional_msg*22+additional_data*55


print('이용요금',fee)

