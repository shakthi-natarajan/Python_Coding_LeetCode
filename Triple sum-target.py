'''
Given an array arr[] of size n and an integer sum, the task is to check if there is a triplet 
in the array which sums up to the given target sum.
'''

def triplet_sum(nums,triplet_sum):
    nums.sort()
    length=len(nums)-1
    triplet=[]
    for i in range(0,length-2):
        target_sum=triplet_sum-nums[i] #target sum is triplet_sum-nums[i] which is the sum we are looking for iin the two pointer technique
        print(f'target sum: {target_sum}')
        left=i+1
        right=len(nums)-1
        while left<right:
            current_sum=nums[left]+nums[right]
            if current_sum<target_sum:
                left+=1
            elif current_sum>target_sum:
                right-=1
            elif current_sum==target_sum:
                triplet.append([nums[i],nums[left],nums[right]])
                break
    print(triplet)

triplet_sum([1,4,6,8,10,45],13)
