class StrongNumber:
    def is_strong_number(self,num):
        dummy = num
        total = 0
        while dummy > 0:
            rem = dummy % 10
            dummy //= 10
            result = 1
            for numbers in range(1,rem+1):
                result *= numbers
            total += result
        if num == total:
            print("strong number")
        else:
            print("not a strong number")

obj = StrongNumber()
num = int(input("enter a number :-"))
obj.is_strong_number(num)