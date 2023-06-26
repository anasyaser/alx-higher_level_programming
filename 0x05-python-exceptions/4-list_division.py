#!/usr/bin/python3
def list_division(lst1, lst2, lst_lenght):
    result = [0] * lst_lenght
    for i in range(lst_lenght):
        try:
            result[i] = lst1[i] / lst2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
            break
        except TypeError:
            print("wrong type")
        finally:
            pass
    return result
