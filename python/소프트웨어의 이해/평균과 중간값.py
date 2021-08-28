def mean(nums):#평균
    average=sum(nums)/len(nums)
    return average
def median(nums):#중간값
    if len(nums)%2 == 0:
        n=len(nums)//2
        return (nums[n]+nums[n-1])/2
    else:
        n=len(nums)//2
        nums.sort()
        return nums[n]

nums=[]
while True:
    num=input('점수 : ')
    if len(num) == 0:
        break
    nums.append(int(num))


#평균
print(mean(nums))
#중간값
print(median(nums))
