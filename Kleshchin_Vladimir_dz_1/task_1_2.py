my_list_cube = []
add_my_list_cube = []
all_sum = 0
n_sum = 0

for i in range(1, 1000, 2):
    my_list_cube.append(i ** 3)

for n, val in enumerate(my_list_cube):
    n_sum = 0
    while val > 0:
        n_sum += val % 10
        val //= 10
    if n_sum % 7 == 0:
        all_sum += my_list_cube[n]

print(all_sum)

all_sum = 0
for m in my_list_cube:
    add_my_list_cube.append(m + 17)

for n, val in enumerate(add_my_list_cube):
    n_sum = 0
    while val > 0:
        n_sum += val % 10
        val //= 10
    if n_sum % 7 == 0:
        all_sum += add_my_list_cube[n]

print(all_sum)

