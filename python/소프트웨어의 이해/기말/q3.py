#진수 변환



#함수 정의
def print_menu():#메뉴출력
    print('*'*6+'진수변환 프로그램'+'*'*6)
    print(' '*6+'1. 10진수 입력')
    print(' '*6+'2. 2진수 입력')
    print(' '*6+'3. 8진수 입력')
    print(' '*6+'4. 16진수 입력')
    print(' '*6+'5. 프로그램 종료')
    print('*'*20)
def get_Decimal():
    deci = int(input('10진수 입력: '))
    return deci
    
def Decimal_to_Binary(x):
    bin=[]
    deci=x
    while deci//2 != 1:
        bin.append(str(deci%2))
        deci = deci //2
    bin.append(str(deci%2))
    bin.append(str(deci//2))
    bin.reverse()
    binary=''
    for i in bin:
        binary += i
    return binary
        
    
def Decimal_to_Octal(x):
    oct=[]
    deci=x
    while deci//8 != 0:
        oct.append(str(deci%8))
        deci = deci//8
    oct.append(str(deci))
    oct.reverse()
    octal=''
    for i in oct:
        octal += i
    return octal
def Decimal_to_Hexadecimal(x):
    hex=[]
    deci=x
    while deci//16 != 0:
        hex.append(str(deci%8))
        deci = deci//8
    hex.append(str(deci))
    hex.reverse()
    hexadeci=''
    for i in hex:
        if i == '10':
            i='A'
        elif i == '11':
            i='B'
        elif i == '12':
            i='C'
        elif i == '13':
            i='D'
        elif i == '14':
            i='E'
        elif i =='15':
            i='F'
        hexadeci += i
    return hexadeci


while True:
    print_menu()
    menu=int(input('menu: '))
    if menu == 1:
        deci = get_Decimal()
    elif menu == 2:
        print('10진수 : %d / 2진수 :'%(deci),Decimal_to_Binary(deci))
        
    elif menu == 3:
        print('10진수 : %d / 8진수 :'%(deci),Decimal_to_Octal(deci))
    elif menu ==4:
        print('10진수 : %d / 16진수 :'%(deci),Decimal_to_Hexadecimal(deci))
    elif menu ==5:
        break




nuber = int(input('10진수를 입력하세요'))
