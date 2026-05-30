class Factorial:
    def factorial_number(self,num):
        total = 1
        for i in range(1,num+1):
            total *= i 
        return total
    
obj = Factorial()
num = int(input('enter a number '))
print(obj.factorial_number(num))