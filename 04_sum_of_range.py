class Sum_of_range:
    def sum(self,num1:int,num2:int):
        count = 0
        for numbers in range(num1,num2+1):
            count += numbers
        return count

obj = Sum_of_range()
num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))
print(obj.sum(num1,num2))

        







