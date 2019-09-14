import itertools


numbers1 = [1, 2, 3, 4]

### Lista 3-elementowa kombinacja

# kombinacja - przyklad 1

print(list(itertools.combinations(numbers1, 3)))

# kombinacja - przyklad 2

combinations_list = []
test_list = []

for i in numbers1:
    for j in numbers1:
        for k in numbers1:
            if i != j and i != k and j != k:
                a = i,j,k
                if sorted(a) not in test_list:
                    test_list.append(sorted(a))
                    combinations_list.append(a)

print(combinations_list)

# permutacja - przykład 1

print(list(itertools.permutations(numbers1)))
