def find_nontwin(inputArray):
    occurences_map = {item: inputArray.count(item)for item in inputArray}
    non_twin_list = []
    for key, value in occurences_map.items(): 
        if value % 2 != 0:
            non_twin_list.append(key)
        
    if not non_twin_list:
        return -1

    return min(non_twin_list)


if __name__ == "__main__":
    print(find_nontwin([1, 1, 2, 3, 3, 4,4]))