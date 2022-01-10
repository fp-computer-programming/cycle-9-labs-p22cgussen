# Charlie CCG 1/9/2022

def double_stuff(lst):
    for i, v in enumerate(lst):
        lst[i] *= 2
    return lst

list1 = [1,2,3,"four",3.5]
print(double_stuff(list1))
