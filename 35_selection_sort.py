class Selection_sort:
    def arrange(self,nums):
        n = len(nums)
        for i in range(0,n):
            min_idx = i 
            for j in range(i+1,n):
                if nums[j] < nums[min_idx]  :
                    min_idx = j
            nums[i],nums[min_idx] = nums[min_idx],nums[i]
        return nums
obj = Selection_sort()
l = [2,1,34,7,5,2,1,56,9]
print(obj.arrange(l))