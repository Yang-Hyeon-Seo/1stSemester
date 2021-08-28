#n번부터 글자 거꾸로 만들기

string = input('문자열을 입력하세요 : ')
number = int(input('문자열의 길이보다 작은 숫자를 입력하세요 : '))

str_lst=[]
for i in string:
    str_lst.append(i)


for i in range(len(string)):
    str1 = str_lst[:number]
    str2 = str_lst[number:]
    str1.reverse()
    str2.reverse()
    new_str=str1+str2
    result=''
    for j in new_str:
        result += j

    print(result)
    number -= 1
