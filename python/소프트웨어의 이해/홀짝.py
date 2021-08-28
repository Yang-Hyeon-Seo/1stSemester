import random
import easygui

number = random.randint(1,100)
if number%2 == 0:
    answer='짝수'
else:
    answer='홀수'

easygui.msgbox('%d'%number)
user = easygui.buttonbox('홀?짝?', choices=['홀수','짝수'])

if user == answer:
    easygui.msgbox('정답')
else:
    easygui.msgbox('오답')
