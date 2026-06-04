class AutomorphicNumber:
    def is_automorphic_number(self,num):
        square = num * num 
        temp = num
        count = 0 
        while temp > 0:
            count += 1
            temp //= 10
        check = square % (10 ** count)
        if num == check:
            print(f"{num} is an Automorphic number ")
        else:
            print(f"{num} is not an Automorphic number ")
        
obj = AutomorphicNumber()
num = int(input("enter a number :-"))
obj.is_automorphic_number(num)