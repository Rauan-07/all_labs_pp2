def permutations_iterative(s):
    result = ['']
    for char in s:
        new_result = []
        for perm in result:
            for i in range(len(perm) + 1):
                new_result.append(perm[:i] + char + perm[i:])
        result = new_result
    for perm in result:
        print(perm)


string = input("Enter a string: ")
permutations_iterative(string)
