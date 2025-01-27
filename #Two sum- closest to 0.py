#Two sum- closest to target say 0

def two_sum(nums):
    nums.sort()
    left=0
    right=len(nums)-1
    closest_sum=999999
    closest_pair=()

    while left<right:
        current_sum=nums[left]+nums[right]

        if abs(current_sum)==0:
            return(nums[left],nums[right])
        
        if abs(current_sum)<abs(closest_sum):
            closest_sum=current_sum
            closest_pair=(nums[left],nums[right])
        elif abs(current_sum)==abs(closest_sum):
            if current_sum>closest_sum:
                closest_pair=(nums[left],nums[right])
        if current_sum<0:
            left+=1
        else:
            right-=1
    return closest_pair

result=two_sum([0, -8, -6, 3])
print(result)

