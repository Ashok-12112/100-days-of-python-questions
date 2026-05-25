class check_even_odd:
    def even_or_odd(self,num:int):
        if num % 2 == 0:
            return 'even'
        else:
            return 'odd'
obj = check_even_odd()
print(obj.even_or_odd(8))