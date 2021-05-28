def persistence(n):
    nums = [int(x) for x in str(n)]
    count = 0 
    while len(nums) != 1:
        n = 1
        for i in nums:
            n*= i
        nums = [int(x) for x in str(n)]
        count+=1
    return count