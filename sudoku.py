import copy
import csv
def return_valid_quadrant(partialSoln,position):
    xCoor = position[0]
    yCoor = position[1]
    allPoss = set([1,2,3,4])
    if xCoor in [0,1] and yCoor in [0,1]:
        exhausted = set([partialSoln[0][0],partialSoln[0][1],partialSoln[1][0],partialSoln[1][1]])
    elif xCoor in [2,3] and yCoor in [0,1]:
        exhausted = set([partialSoln[2][0],partialSoln[3][1],partialSoln[3][0],partialSoln[2][1]])
    elif xCoor in [0,1] and yCoor in [2,3]:
        exhausted = set([partialSoln[0][2],partialSoln[1][3],partialSoln[0][3],partialSoln[1][2]])
    else:
        exhausted = set([partialSoln[2][3],partialSoln[3][2],partialSoln[2][2],partialSoln[3][3]])
    # print exhausted
    if 0 in exhausted:
        exhausted.remove(0)
    valid = allPoss - exhausted
    return valid

def return_valid_row(partialSoln,position):
    xCoor = position[0]
    allPoss = set([1,2,3,4])
    exhausted = set(partialSoln[xCoor])
    if 0 in exhausted:
        exhausted.remove(0)
    valid = allPoss-exhausted
    return valid

def return_valid_column(partialSoln,position):
    xCoor = position[0]
    yCoor = position[1]
    allPoss = set([1,2,3,4])
    exhausted = set([partialSoln[0][yCoor],partialSoln[1][yCoor],partialSoln[2][yCoor],partialSoln[3][yCoor]])
    if 0 in exhausted:
        exhausted.remove(0)
    valid = allPoss-exhausted
    return valid

def return_valid(partialSoln,position):
    quadrant = return_valid_quadrant(partialSoln,position)
    row = return_valid_row(partialSoln,position)
    col = return_valid_column(partialSoln,position)
    validFinal = quadrant & row & col
    return validFinal
    
def fill_sudoku(arr, position):
    newFrontier = []
    for partialSoln in arr:
        validOptions = return_valid(partialSoln,position)
        for option in validOptions:
            temp = copy.deepcopy(partialSoln)
            temp[position[0]][position[1]] = option
            newFrontier.append(temp)
    return newFrontier

arr = [[[0]*4 for _ in range(4)]]
print arr
for xCoor in [0,1,2,3]:
    for yCoor in [0,1,2,3]:
        position = [xCoor,yCoor]
        arr = fill_sudoku(arr,position)
        
writer = csv.writer(open("filename.csv", "wb"),quoting=csv.QUOTE_NONNUMERIC)
for sol in arr:
    writer.writerows(sol)
writer.close()
