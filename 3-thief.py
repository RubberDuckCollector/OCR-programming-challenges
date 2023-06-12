import itertools

def find_combinations(num):

    num = str(num)

    return list(itertools.permutations(num))

print(find_combinations(1234))
