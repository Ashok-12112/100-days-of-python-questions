class PerfectNumber:
    def is_perfect_number(self,num):
        total = 0
        for i in range(1,num):
            if num % i == 0:
                total += i
        if num == total:
            print(f'{num} is a perfect number')
        else:
            print(f'{num} is not a perfect number')

        
obj = PerfectNumber()
num = int(input("enter a number :-"))
obj.is_perfect_number(num)
