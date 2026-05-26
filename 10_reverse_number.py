class ReverseNumber:
    def number(self,num):
        reverseNum = 0
        while num > 0:
            rem = num % 10 
            reverseNum = reverseNum * 10 + rem
            num //= 10
        return reverseNum

obj = ReverseNumber()
num = int(input("enter a number :"))
print(obj.number(num))