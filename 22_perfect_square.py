class PerfectSquare:
    def is_perfect_square(self,num):
        is_perfect = False
        for i in range(1,num+1):
            if i * i == num:
                is_perfect = True
                break
        if is_perfect:
            print(f'{num} is a perfect square')
        else:
            print(f'{num} is not a perfect square')
obj = PerfectSquare()
num = int(input('enter a number'))
obj.is_perfect_square(num)