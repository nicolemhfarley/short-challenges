# A function that looks at the number of times given letters appear in a document. 
# The output is in a dictionary.

def letter_counter(path_to_file, letters_to_count):
    ''' Returns a dictionary with the number of times specified letters appear in a file'''
    letter_counts = {}
    with open(path_to_file) as file:
        word_list = file.read().split()
    
    letters = []
    for letter in letters_to_count:
        letters.append(letter)
    
    for word in word_list:
        for letter in word:
            if letter in letters and letter not in letter_counts.keys():
                letter_counts[letter] = 1
            elif letter in letters and letter in letter_counts.keys():
                letter_counts[letter] = letter_counts[letter] + 1
                
    return(letter_counts)
    
