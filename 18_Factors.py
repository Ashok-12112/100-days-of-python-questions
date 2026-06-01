class Factors:
    def is_factors(self,num):
        for numbers in range(1,num+1):
            if num % numbers == 0:
                print(numbers)

obj = Factors()
num = int(input("enter a number :-"))
obj.is_factors(num)