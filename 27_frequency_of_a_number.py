class Frequency:
    def frequency_number(self,l):
        d = {}
        for i in range(0,len(l)):
            if l[i] in d :
                d[l[i]] += 1
            else:
                d[l[i]] = 1
        print(d)
obj = Frequency()
l = [1,2,3,3,2,3,4,5,6]
obj.frequency_number(l)