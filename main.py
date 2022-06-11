print('Hello world')

new_list = [7, 6, 2, 43, 33, 15, 9, 77, 56, 5]
N = len(new_list)
n = 1
myMax = new_list[0]
myMin = new_list[0]

for i in range(N):
    if new_list[i] > myMax: myMax = new_list[i]
    if new_list[i] < myMin: myMin = new_list[i]

print('Max', myMax, 'Min', myMin)


def razbivka(l, fel, lel):
    j = fel
    i = j
    while j < lel:
        if l[j] <= l[lel]:
            l[i], l[j] = l[j], l[i]
            i += 1
        j += 1

    l[i], l[lel] = l[lel], l[i]
    return i


def my_sort(l, fel, lel):
    if fel >= lel:
        return
    r = razbivka(l, fel, lel)
    my_sort(l,fel,r-1)
    my_sort(l, r+1, lel)

def final_sort(l):
    my_sort(l, 0, len(l)-1)


print(new_list)
final_sort(new_list)
print(new_list)
