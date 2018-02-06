""" Given two arrays a1 and a2 of positive integers find the common elements between them and return a set of the elements that have a sum or difference equal to either array length.

All elements will be positive integers greater than 0
If there are no results an empty set should be returned
Each operation should only use two elements
Examples

a1 = [1, 2, 3, 4, 5, 6]
a2 = [1, 2, 4, 6, 7, 8, 9, 10]
should return {2, 4, 6} because all three integers exist in both arrays and a1 has a length of 6 (2+4) and a2 has a length of 8 (2+6).

a1 = [1, 2, 3, 5, 10, 15]
a2 = [1, 2, 3, 4, 5, 6, 10, 12, 15, 16]
should return {1, 5, 15} because all 3 integers exist in both arrays and a1 has a length of 6 (1+5) and a2 has a length of 10 (15-5). """

def common_el(a1, a2):
	# first compare all elements in both arrays.  add any common elements to a list, then filter 
		
	common = []
    results = []
    for i in range(len(a1)):
        for j in range(len(a2)):
            if a2[j] == a1[i]:
                common.append(a2[j])
    if common == None:
        return {}
        
    for i in range(len(common)):
        for j in range(len(common)):
            if ((common[j] + common[i] == len(a1)) or (common[j] + common[i] == len(a2))) and j != i:
                results.append(common[j])
                results.append(common[i])
            elif ((common[j] - common[i] == len(a1)) or (common[i] - common[j] == len(a1))) and j != i:
                results.append(common[j])
                results.append(common[i])
            elif ((common[j] - common[i] == len(a2)) or (common[i] - common[j] == len(a2))) and j != i:
                results.append(common[j])
                results.append(common[i])
    results = set(results)
    return results

	
arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [1, 2, 4, 6, 7, 8, 9, 10]

a1 = [1, 2, 3, 5, 10, 15]
a2 = [1, 2, 3, 4, 5, 6, 10, 12, 15, 16]

x = common_el(a1, a2)
print(x)
















