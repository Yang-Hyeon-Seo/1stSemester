f=open('score.txt','w')
while True:
    score=input('점수')
    if len(score) == 0:
        break
    f.write(score+'\n')
f.close()
f=open('score.txt','r')

lines=f.readlines()

scores=[]
for i in lines:
    score=int(i)
    scores.append(score)
    
maximum = max(scores)
print(maximum)
    
all = sum(scores)
average = all/len(scores)
print(average)
