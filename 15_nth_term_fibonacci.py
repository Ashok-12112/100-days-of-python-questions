class Fibonacci:
    def num(self, number):
        a, b = 0, 1
        for i in range(1, number):  # loop runs (number-1) times to reach Nth term
            a, b = b, a + b
        return a

obj = Fibonacci()
num = int(input("Enter a number: "))
result = obj.num(num)
print(f"The {num}th Fibonacci term is: {result}")