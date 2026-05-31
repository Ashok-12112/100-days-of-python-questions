class Power:
    def power_of_a_number(self,base, exponent):
        result = 1
        for i in range(exponent):
            result *= base
        return result
    
obj = Power()
base = int(input('enter base'))
exponent = int(input('enter exponent'))
print(obj.power_of_a_number(base,exponent))