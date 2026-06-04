class HarshadNumber:
    def is_harshad_number(self,num):
        dummy = num 
        sum = 0
        while dummy > 0 :
            rem = dummy % 10
            sum += rem
            dummy //= 10
        if num % sum == 0 :
            print(f"{num} is a harshad number")
        else:
            print(f"{num} is not a harshad number")

obj = HarshadNumber()
num = int(input("enter a number -"))
obj.is_harshad_number(num)