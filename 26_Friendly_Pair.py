class Friendly_Pair:
    def is_friendly_pair(self,num1,num2):
        num1_sum = 0
        for i in range(1,num1):
            if num1 % i == 0:
                num1_sum += i
        num2_sum = 0
        for i in range(1,num2):
            if num2 % i == 0:
                num2_sum += i
        if num1 == num2_sum and num2 == num1_sum:
            print(f"{num1 , num2 } are friendly pair")
        else:
              print(f"{num1 , num2 } are not  friendly pair")

obj = Friendly_Pair()
num1 = int(input("enter first number - "))
num2 = int(input("enter second number - "))
obj.is_friendly_pair(num1,num2)