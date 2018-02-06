""" count number of pairs of anagrams in a list of strings. 
"""

def anagrams(array):

	# break down each word into a separate list
	# sort contents of sublists
	# compare contents of each sublist and increment a counter if there is a match
	letters_list = []
	for arr in array:
		arr = sorted(list(arr))
		letters_list.append(arr)

	match_list = []
	# compare entire list to each item in the list
	for i in range(len(letters_list)):
		for j in range(len(letters_list)):
			if letters_list[j] == letters_list[i] and j != i and (j, i) not in match_list and (i, j) not in match_list: # add only unique pairs of items
				match_list.append((j, i))
				
	return len(match_list)
		

word_list = ["bat", "cat", "rat", "tar", "tab", "star", "rats", "arts"] # --> 2

x = anagrams(word_list)
print(x)
