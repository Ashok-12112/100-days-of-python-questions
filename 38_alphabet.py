class Check_alphabet:
    def is_alphabet(self,character):
        if character.isalpha():
            return 'alphabet'
        else:
            return 'not alphabet'

obj = Check_alphabet()
print(obj.is_alphabet('u'))