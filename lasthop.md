Lucy loves to play the Hop, Skip and Jump game. Given an N\*M matrix and starting from cell(1,1), her challenge is to hop in an anti-clockwise direction and skip alterante cells. The goal is to find out the last cell she would hop onto.

Write an algorithm to find the last cell Lucy would hop onto after moving anti-clockwise and skipping alternate cells.

Input: The first line of input consists of two integers -matric_row and matrix_col, representing the numbers of rows(N) and the numbers of columns(M) in the matrix, respectively.
The next M lines consist of N space separated integers representing the elements in each cells of the matrix.

Example:

3 3
29 8 37
15 41 3
1 10 14

Output:
41

Explanation:
Lucy starts with 29, skips 15, hops onto 1, skip 10, hops onto 14, skips 3, hops onto 37, skips 8 and finally hops onto 41.
So, the output is 41.
