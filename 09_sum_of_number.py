class Number:
    def sum_of_number(self,num):
        count = 0
        while num > 0 :
            rem = num % 10
            count += rem
            num//=10
        return count
obj = Number()
num = int(input('enter a number:'))
print(obj.sum_of_number(num))