def is_member(val, temp_list):
    if temp_list.count(val) >= 1:
        return True
    else:
        return False


if __name__ == "__main__":
    x = eval(input("Enter value: "))
    a = list(eval(input("Make list: ")))
    print(is_member(x, a))
