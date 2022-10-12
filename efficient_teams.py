# each team has exactly two candidates
# total candidates = n
# skill of each candidate = skill[i]
# no of teams = n/2
# efficiency of team = product of skill level of two members i.e 1 * 3 = 3 for skills[1,3]
# sum of efficiencies of teams that can be formed
# condition : total skill of each team is same, if there is no way to satisfy this condition,return -1
# eq: [1,2,3,2]


from functools import reduce

def getTotalEfficiency(skill):
    n = len(skill)
    subset_list = []
    # if odd number of skill then return -1
    if n % 2 != 0:
        return -1
    # finding subsets with two skills
    else:
        for i in range(len(skill)):
            for j in range(len(skill)):
                if i == j:
                    continue
                else:
                    new_list = [skill[i], skill[j]]
                    if new_list not in subset_list :
                        subset_list.append(new_list)
                        
    # finding list of duplicate sets 
    duplicates_to_remove = []
    for i in range(len(subset_list)):
        for j in range(i+1, len(subset_list)):
            if set(subset_list[i]) == set(subset_list[j]):
                duplicates_to_remove.append(subset_list[j])

    # remove duplicates from subset_list
    for m in range(len(duplicates_to_remove)):
       subset_list.remove(duplicates_to_remove[m])
    
    # creating a new dict whose key is a tuple of skills and value is sum of tuple
    dict_a = {}
    for l in range(len(subset_list)):
        dict_a[tuple(subset_list[l])] = sum(subset_list[l])

    # creating a new dict whose key is an int and value is a set of tuple elements
    dict_b = {}
    for key, value in dict_a.items():
        dict_b.setdefault(value,set()).add(key)

    # finding teams whose sum of skills is same
    final_team_list = list(filter(lambda x: len(x) > 1, dict_b.values()))
    final_team_set = final_team_list[0]

    # finding the sum of efficiency of newly formed teams
    sum_of_efficiency = 0
    for m in range(len(final_team_set)):
        popped_list = list(final_team_set.pop())
        result = reduce((lambda x, y: x * y),popped_list)
        sum_of_efficiency += result
    return sum_of_efficiency
    
if __name__ == "__main__":
    print(getTotalEfficiency([1, 2, 3, 2]))
    print(getTotalEfficiency([4, 3, 1,6]))
    print(getTotalEfficiency([3, 3, 3,2,5,1]))

    