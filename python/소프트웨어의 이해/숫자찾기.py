#팩토리얼 함수
def pac(n):
    if n == 1:
        return 1
    else:
        mul=n*pac(n-1)
        return mul


#위치 반환 함수
def search(lst, key):
    if len(lst)==0:#리스트가 비었으면, False
        return False
    elif lst[0]==key:#리스트가 있는 것임, 리스트의 첫번째 것
        return True
    else:
        return search(lst[1:], key)

#개수 세기
def searchn(lst, key):
    if not lst:#빈 리스트
        return 0
    elif lst[0] == key:
        n=searchn(lst[1:], key)#재귀함수, lst[1]부터 끝까지 다시 넣는다
        #다시 했을 떄 만약 빈 리스트면 n=0, 빈리스트가 아니고 key와 같다면 n에다가 1을 더하고
        #다시 n을 찾는다...계속 찾아서 결국 n=0이 되는 순간을 만나게 된다.
        return n+1
    else:#길이가 0도 아니고 key와도 같지 않는 경우, n을 리턴하고
        #n은 하나씩 돌아가면서 1개씩 더해지거나 말거나 하다가 결국 0을 만나고 리턴된다
        n=searchn(lst, key)
        return n

#인덱스 찾기
def searchi(lst, key):
    if len(lst)==1:
        n=0
    if len(lst) == 0:
        return False
    elif lst[0] == key:
        n=searchi(lst, key)
        return n
    else:
        n=searchi(lst, key)
        n+=1
        return searchi(lst, key)
#n이 각자 정의되어야함

print(pac(5))

lst=[1,2,3,4,5,2]
search(lst, 2)
searchn(lst, 2)
#searchi(lst, 2)
