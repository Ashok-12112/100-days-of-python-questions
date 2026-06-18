class Position_fibonacchi:
    def check_position(self,num):
        if num == 0 or num == 1:
            return num
        return self.check_position(num-1) + self.check_position(num-2)    
obj = Position_fibonacchi()
print(obj.check_position(6))