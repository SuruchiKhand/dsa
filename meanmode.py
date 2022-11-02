def meanMode(inputArr):
    sum = 0
    for i in range(len(inputArr)):
       sum += inputArr[i]
    
    #finding mean of the array
    mean_of_nums = sum // len(inputArr)

    count_map = {}
    count_map = {item: inputArr.count(item) for item in inputArr}
    
    # finding mode of the array
    highest_frequency = max(count_map.values())
    for key, value in count_map.items():
        if highest_frequency == value:
            mode_of_nums = key

    return str(mean_of_nums) + " " + str(mode_of_nums)

if __name__ == "__main__":
    print(meanMode([1,2,3,7,2]))