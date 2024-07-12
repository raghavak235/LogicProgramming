# DE CODE
# Move all the o to the starting and all 1 to the end.
def zerosAndOnes(nums:list)-> None:
    size=len(nums)
    first=0
    last = size-1
    while first<last:
        if nums[first]==0:
            first +=1
        if nums[last]==1:
            last -=1
        if nums[first]==1 and nums[last]==0:
            nums[first], nums[last]= nums[last], nums[first]
    print(nums)

zerosAndOnes([1,0,1,1,0,0,1])