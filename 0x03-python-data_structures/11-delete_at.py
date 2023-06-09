#!/usr/bin/python3
def delete_at(my_lst=[], idx=0):
    if 0 <= idx < len(my_lst):
        del my_lst[idx]
    return my_lst

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    newlst = delete_at(lst, -2)
    print(newlst)
    new2 = delete_at(lst, 5)
    print(newlst)
