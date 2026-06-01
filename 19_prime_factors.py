class PrimeFactors:
    def prime_factors(self,num):
        i = 2
        while i <= num:
            if num % i == 0:
                print(i)
                num = num // i 
            else:
                i += 1

obj = PrimeFactors()
num = int(input('enter a number :-'))
obj.prime_factors(num)