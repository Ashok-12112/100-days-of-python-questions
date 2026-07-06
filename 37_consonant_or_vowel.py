class Check:
    def consonant_or_vowel(self,singleCharacter):
        vowel = 'aeiouAEIOU'

        if singleCharacter in vowel:
            return 'Vowel'
        else:
            return 'Consonant'
    
obj = Check()
print(obj.consonant_or_vowel('a'))

