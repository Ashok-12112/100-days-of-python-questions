class Checknumber:
    def positive_or_negative(self,num:int):
        if num >= 0:
            return "positive"
        else:
            return "negative"
        
obj = Checknumber()
print(obj.positive_or_negative(8))
