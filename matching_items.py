def multiple_of_3(num1, num2):
	'''check if sum of 2 numbers is a multiple of 3
	'''
	if (num1 + num2) % 3 == 0:
		return True
	else:
		return False

def both_vowels_or_consonants(letter1, letter2):
	'''check if 2 letters are both vowels or both consonants.
	'''
	vowels = ('a', 'e', 'i', 'o', 'u')
	if letter1 in vowels and letter2 in vowels:
		return True
	elif letter1 not in vowels and letter2 not in vowels:
		return True
	elif letter1 in vowels and letter2 not in vowels:
		return False
	elif letter1 not in vowels and letter2 in vowels:
		return False
        
def matching_pairs(data_list):
    '''input: list of tuples (letter, number).
    output: list of the matching pair referenced by their index (index_A, index_B) with no repeats.'''
    
    comparison_list = []
    match_list = []
    unique_match_list = []
    for item in data_list:
        comparison_list.append(item)
               
    for item in data_list: # check against comparison_list
        for entry in comparison_list:
            if item == entry: # if they are identical, move on to next iteration
                continue
            elif both_vowels_or_consonants(item[0], entry[0]) == True and multiple_of_3(item[1], entry[1]) == True:
                match_pairs = (item.index, entry.index)
                match_list.append(match_pairs)
    for pair in match_list:
        if pair not in unique_match_list and (pair[1],pair[0]) not in unique_match_list:
            unique_match_list.append(pair)
                
    return unique_match_list

data = [('a', 4), ('b', 5), ('c', 1), ('d', 3), ('e', 2), ('f',6)]
matching_pairs(data)
     

