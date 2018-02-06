"""
reverses the input string but keeps the same spacing as original string
"""
def solve(s):
    s_list = list(s)
    rev = s[::-1]
    rev_s = rev.replace(" ", "")
    rev_list = list(rev_s)
    new_list = []
           
    i = 0
    j = 0
    while i < len(s_list):
        if s_list[i] != ' ':
            new_list.append(rev_list[j])
            i += 1
            j += 1
        elif s_list[i] == ' ':
            new_list.append(' ')
            i += 1
            
    answer = ''.join(new_list)
    
    return str(answer)
            
