class Reverse_list:
    def reverse_list(self,l,left,right):
        if left >= right:
            return 
        l[left],l[right] = l[right],l[left]
        return self.reverse_list(l,left+1,right-1)

obj = Reverse_list()
l = [1,2,3,4,5]
obj.reverse_list(l,2,len(l)-1)
print(l)
