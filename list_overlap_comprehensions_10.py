a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

if len(a) > len(b):
    l1 = a
    l2 = b
else:
    l1 = b
    l2 = a
res = list({x for x in l1 if x in l2})
print(res)