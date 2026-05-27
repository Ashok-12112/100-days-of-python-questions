class Palindrome:
    def is_palindrome(self,num):
        dummy = num
        revNum = 0
        while dummy > 0:
            rem = dummy % 10
            revNum = revNum * 10 + rem 
            dummy //= 10
        if num == revNum:
            return f"{num} is palindrome"
        else:
            return f"{num} is not palindrome"
    
obj = Palindrome()
num = int(input("enter number"))
print(obj.is_palindrome(num))