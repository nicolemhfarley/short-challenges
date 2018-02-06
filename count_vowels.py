"""Write a function count_vowels to count the number of vowels in a given string.

Notes:
Return nil or None for non-string inputs.
Return 0 if the parameter is omitted."""

def count_vowels(s = ''):
    
    vowels = ('a', 'e', 'i', 'o', 'u')    
    
    if isinstance(s, str):           
        s_list = list(s)
        print(s_list)
        vowel_count = 0        
        for char in s_list:
            if char.isalpha() and char.lower() in vowels:
                vowel_count += 1
            else:
                continue
        return vowel_count
    elif s == 0:
        return None
    elif not s: 
        return None
    else:
        return None
    
