# Separeting positive numbers & negetive numbers >
p_list = []
n_list = []
for i in range(-5,10):
    if i > 0:
        p_list.append(i)
    if i < 0:
        n_list.append(i)
print(p_list)
print(n_list)
