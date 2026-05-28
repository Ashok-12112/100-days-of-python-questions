class Fibonacci:
    def num(self,number):
        a,b = 0,1
        for i in range(number):
            print(a)
            a,b = b,a+b

obj = Fibonacci()
num = int(input("enter a number :-"))
obj.num(num)

