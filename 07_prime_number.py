class Prime:
    def isprime(self,num):
        count = 0
        for i in range(1,num//2+1):
            if num % i == 0:
                count += 1
        if count == 1:
            return f"{num} is a prime number"
        else:
            return f"{num} is not a prime number"
    
obj = Prime()
num = int(input("enter a number :"))
print(obj.isprime(num))