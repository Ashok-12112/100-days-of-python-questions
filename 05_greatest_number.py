class Greatest_numbers:
    def check_number(self,num1:int,num2:int):
        if num1>num2:
            return f"{num1} is greater"
        elif num2>num1:
            return f"{num2} is greater"
        else:
            return "numbers are equal"

obj = Greatest_numbers()
num1 = int(input('enter 1st number'))
num2 = int(input('enter 2nd number'))
print(obj.check_number(num1,num2))