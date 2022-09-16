n = [1, 3, 7, 2, 4, 5, 9, 8, 6]


def sorting_by_insert(n):
    for i in range(1, len(n)):
        while i > 0 and n[i - 1] < n[i]:
            n[i], n[i - 1] = n[i - 1], n[i]
            i -= 1
    print(n)


sorting_by_insert(n)
