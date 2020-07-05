#codewars challenge

def is_merge(s, part1, part2):
    #converts all strings to lists
    s = [i for i in s]
    combined = [i for i in part1] + [i for i in part2]

    #edge case
    if len(combined) <  len(s):
        return False

    #iterate between two lists
    for i in s:
        if i not in combined:
            return False        
    return True
	
print(ismerge('codewars', 'cdea', 'owrs')