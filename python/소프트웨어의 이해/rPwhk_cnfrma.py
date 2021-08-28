#은행 계좌 프로그램, 출금액 작성

balance = 0
name=input('사용자 이름 : ')
amount_in = int(input('입금액 '))
amount_out = int(input('출금액'))

balance += amount_in
balance -= amount_out
    
print(balance)
