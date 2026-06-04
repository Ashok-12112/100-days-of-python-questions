class AbundantNumber:
    def is_abundant_number(self,num):
        total = 0
        for i in range(1,num):
            if num % i == 0:
                sum += i
        if num < sum :
            print(f"{num} is a abundant number")
        else:
            print(f"{num} is not a abundant number")

obj = AbundantNumber()
num = int(input('enter a number - '))
obj.is_abundant_number(num)

        