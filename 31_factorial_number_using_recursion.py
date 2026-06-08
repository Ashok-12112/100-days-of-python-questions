class Factorial:
    def factorial_numbers(self,num):
        if num == 1 or num == 0:
            return 1
        return num * self.factorial_numbers(num-1)
    
obj = Factorial()
print(obj.factorial_numbers(5))
