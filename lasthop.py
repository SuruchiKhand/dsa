def findLastHop(inputArr):
    flag = True

    minColumn = 0
    maxColumn = len(inputArr) - 1
    maxRow = len(inputArr) - 1
    minRow = 0
    rowCursor = 0
    colCursor = 0


    while(flag):


        #Move down
        while(True):
            rowCursor += 2
            if (rowCursor >= maxRow):
                rowCursor = maxRow
                #minRow += 1
                break

        #Move left
        while(True):
            colCursor += 2
            if (colCursor >= maxColumn):
                colCursor = maxColumn
                minColumn += 1
                break

        #Move up
        while(True):
            rowCursor -= 2
            if(rowCursor <= minRow):
                rowCursor = minRow
                maxRow -= 1
                minRow += 1
                break

        #Move right
        while(True):
            colCursor -= 2
            if(colCursor <= minColumn):
                colCursor = minColumn
                maxColumn -= 1
                break

        if(minColumn >= maxColumn or minRow >= maxRow ):
            flag = False

        print(inputArr[rowCursor+1][colCursor])


if __name__ == "__main__":
    findLastHop([[29, 8, 37], [10, 41, 3], [1, 10, 14]])