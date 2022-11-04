def maxSum(inputArr):
	
    numjars = len(inputArr)
    new_arr = [0 for x in range(numjars)]
    new_arr[0] = inputArr[0]
    new_arr[1] = max(inputArr[0], inputArr[1])

    for i in range(2, numjars):
        new_arr[i] = max(new_arr[i - 1], inputArr[i] + new_arr[i-2])

    return new_arr[-1]

if __name__ == "__main__":
    print(maxSum([5,30,99,60,5,10]))