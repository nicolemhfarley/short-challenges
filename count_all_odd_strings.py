"""
Given a string of integers, return the number of odd-numbered substrings that can be formed.

For example, in the case of "1341", they are 1, 1, 3, 13, 41, 341, 1341, a total of 7 numbers.

solve("1341") = 7"""

def solve(s):
    
    # make a list of all possible numbers then filter for odd numbers
    s_list = list(s)
    all_s = []    
    i = len(s_list)
    while i > 0:
        for j in range(len(s_list)):
            all_s.append(s[j:i])   
        i -= 1      
    ints_list = [int(entry) for entry in all_s if entry]
    counter = 0   
    for num in ints_list:
        if num % 2 != 0:
            counter += 1
    return counter
