l = "128540374583"
new_l = []

for i in l:
    new_l.append(int(i))

for k in range(1, len(new_l)):
    while k > 0 and new_l[k] > new_l[k-1]:
        new_l[k], new_l[k-1] = new_l[k-1], new_l[k]
        k -= 1
print(new_l)