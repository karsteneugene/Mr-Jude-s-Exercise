def list_tuple(temp_sample):
    sample_list = list(temp_sample.split(","))
    sample_tuple = tuple(temp_sample.split(","))
    print("List:", sample_list)
    print("Tuple:", sample_tuple)


if __name__ == "__main__":
    sample = input("Enter numbers using commas as separators: ")
    print("")
    list_tuple(sample)
