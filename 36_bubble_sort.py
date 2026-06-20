class Bubble_sort:
    def ordering(self,list_num):
        n = len(list_num)
        for i in range(n-2,-1,-1):
            for j in range(0,i+1):
                if list_num[j] > list_num[j+1]:
                    list_num[j],list_num[j+1] = list_num[j+1],list_num[j]
        return list_num

obj = Bubble_sort()
list_num = [2,1,4,6,3,1]
print(obj.ordering(list_num))