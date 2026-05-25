class PrimeNumber:
    def isprime(self,st,end):
        if st > 1:
            for i in range(st,end+1):
                for j in range(2,i):
                    if i % j == 0:
                        break
                else:
                    print(i)
        else:
            return "start number must be greater than 1"
            
obj = PrimeNumber()
start = int(input('enter start number :'))
end = int(input("enter end number : "))
obj.isprime(start,end)


       