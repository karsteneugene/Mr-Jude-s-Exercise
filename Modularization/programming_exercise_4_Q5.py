def overlapping(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if lst1.count(j) >= 1:
                return True
            elif lst2.count(i) >= 1:
                return True
            else:
                return False


if __name__ == "__main__":
    list_1 = list(eval(input("Make list 1: ")))
    list_2 = list(eval(input("Make list 2: ")))
    print(overlapping(list_1, list_2))
