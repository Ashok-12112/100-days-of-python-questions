class Armstrong_number:
    def is_armstrong(self,start,end):
        for num in range(start,end+1):
            dummy = num
            l = len(str(num))
            sum = 0
            while dummy > 0 :
                sum += (dummy % 10) ** l
                dummy //= 10
            if sum == num:
                print(num)

obj = Armstrong_number()
st = int(input("enter start number"))
end = int(input("enter end number"))
obj.is_armstrong(st,end)

