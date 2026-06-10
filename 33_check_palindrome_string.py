class CheckPalindrome:                        
    def is_palindrome(self, name):            
        left = 0
        right = len(name) - 1
        is_palindrome = True                

        while left < right:
            if name[left] != name[right]:
                is_palindrome = False
                break
            left += 1
            right -= 1

        if is_palindrome:                   
            return f'{name} is palindrome'
        else:
            return f'{name} is not palindrome'


obj = CheckPalindrome()                       
print(obj.is_palindrome('nitin'))               
           
