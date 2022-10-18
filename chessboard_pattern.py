def chessboard(inputNum: int):
    chessboard = [[0 for i in range(inputNum)] for y in range(inputNum)] # using list comprehension to get 2D array
    print("chessboard", chessboard)

    for i in range(inputNum):
        for j in range(inputNum):
            if i % 2 == 0:
                if j % 2 == 0:
                    chessboard[i][j] = "W"
                else:
                    chessboard[i][j] = "B"
            else:
                if j % 2 == 0:
                    chessboard[i][j] = "B"
                else:
                    chessboard[i][j] = "W"
   
    chessboard_str = ""
    for rows in chessboard:
        for columns in rows:
            chessboard_str = chessboard_str + columns + " "
        chessboard_str += "\n"
    return chessboard_str

if __name__ == "__main__":
    print(chessboard(5))