nums=[0,1,0,3,12]
p0=0
curr=0
p1=1
while p1<len(nums):
    if nums[curr]==0 and nums[p1]!=0:
        nums[p1],nums[p0]=nums[p0],nums[p1]
        curr=curr+1
        p1=p1+1
        p0=p0+1
    else:
        curr=curr+1
        p1=p1+1
print(nums)
