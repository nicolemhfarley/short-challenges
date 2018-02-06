"""
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
""" 

def iq_test(numbers):

    numbers_list = numbers.split()
    new_list = []
    for i in numbers_list:
        num = int(i)
        new_list.append(num)

    evens = [num for num in new_list if num % 2 ==0]
    odds = [num for num in new_list if num % 2 != 0]
    
    if len(evens) == 1:
        for num in new_list:
            if num % 2 == 0:
                return (new_list.index(num) +1)
    elif len(odds) == 1:
        for num in new_list:
            if num % 2 != 0:
                return (new_list.index(num) + 1)
