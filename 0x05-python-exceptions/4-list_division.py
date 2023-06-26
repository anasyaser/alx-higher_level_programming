#!/usr/bin/python3
def list_division(lst1, lst2, lst_lenght):
    result = [0] * max(len(lst1), len(lst2))
    for i in range(len(result)):
        try:
            result[i] = lst1[i] / lst2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
            break
        except (ValueError, TypeError):
            print("wrong type")
        finally:
            pass
    return result
