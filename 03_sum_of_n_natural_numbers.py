class Sum_of_n_natural_numbers:
    def sum(self,num:int):
        count = 0
        for n in range(1,num+1):
            count+=n
        return count

obj = Sum_of_n_natural_numbers()
number = int(input('enter a number'))
print(obj.sum(number))
