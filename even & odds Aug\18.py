#printing odds evens from 1 list >

list1 = []
e_list = []
o_list = []
for i in range(100):
    if i%2 != 0 :
        #print(i, end = "  ") 
        o_list.append(i)
    if i%2 == 0 :
        #print(i, end = "  ") 
        e_list.append(i)
print('Even_list: \n',e_list)
print('Odd_list: \n',o_list)
