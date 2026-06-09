def remove_duplicates(l):
    uni = []
    for x in l:
        if x not in uni:
            uni.append(x)
    return uni

l = [1, 1, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7]

a = list(set(l))
print(a)

print(remove_duplicates(l))