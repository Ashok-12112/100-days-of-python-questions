class ArmstrongNumber:
    def is_armstrong(self,num):
        dummy = num
        length = len(str(num))
        val = 0

        while dummy > 0 :
            val += (dummy % 10) ** length
            dummy //= 10
        if val == num:
            return f"{num} is a armstrong number"
        else:
            return f"{num} is not a armstrong number"
        
obj = ArmstrongNumber()
num = int(input('enter a number'))
print(obj.is_armstrong(num))
            