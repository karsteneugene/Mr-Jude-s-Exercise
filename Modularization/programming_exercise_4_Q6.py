def histogram(lst):
    for i in lst:
        print(i * "*")


if __name__ == "__main__":
    mylist = list(eval(input("Make a list: ")))
    histogram(mylist)
