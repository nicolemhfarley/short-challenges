# colored triangles challenge 7th kyu - codewars

def triangle(row):
    
    testrow = row  
    if row == 'R' or row == 'B' or row == 'G':
        return row 
    while len(testrow) > 1:
        first = 0
        second = 1
        next_row = ''
        i = 0
        for i in range(len(testrow)-1):
            if testrow[first] == testrow[second]:
                next_row += testrow[first]
                first += 1
                second += 1
                i += 1
            elif (testrow[first] == 'B' and testrow[second] == 'G') or (testrow[first] =='G' and testrow[second] == 'B'):
                next_row += 'R'
                first += 1
                second += 1
                i += 1
            elif (testrow[first] == 'B' and testrow[second] == 'R') or (testrow[first] =='R' and testrow[second] == 'B'):
                next_row += 'G'
                first += 1
                second += 1
                i += 1
            elif (testrow[first] == 'G' and testrow[second] == 'R') or (testrow[first] =='R' and testrow[second] == 'G'):
                next_row += 'B'
                first += 1
                second += 1
                i += 1
        testrow = next_row        
    
    if len(testrow) == 1:
        return testrow
