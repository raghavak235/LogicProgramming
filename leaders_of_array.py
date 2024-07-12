# DE CODE
#  l=[16,17,4,3,5,2]
#  the leader in the list will be the num where the right side elements are sum_of_2_small
# output:l=[2,5,17]

def leader_list(nums):
    size = len(nums)
    ans=[nums[-1]]
    max = nums[size-1]
    for i in range(size-2, -1,-1):
        if nums[i]>max:
            max=nums[i]
            ans.append(nums[i])

    print(ans)

leader_list([16,17,4,3,5,2])
