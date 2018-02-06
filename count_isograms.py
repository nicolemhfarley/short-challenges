def count_isograms(list_of_words):
    '''counts number of isograms in a list of strings. 
    Input:list_of_words: list of strings
    Returns: count of isograms as an int
    '''
    counter = 0
    for word in list_of_words:
        letter_list = []
        for letter in word:
            if letter in letter_list:
                continue
            if letter not in letter_list:
                letter_list.append(letter)
        if len(letter_list) == len(word):
            counter += 1
    return counter
