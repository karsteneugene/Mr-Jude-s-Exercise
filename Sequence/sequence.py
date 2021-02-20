import re


def name_sequence(filename):
    with open(filename, 'r') as d:
        names = re.findall('\w+', d.read())
    current_sequence = []
    longest_sequence = []

    def starts_with(last_letter, temp_list):
        for temp_name in temp_list:
            if temp_name.startswith(last_letter):
                return temp_list.index(temp_name)
        return False

    for name in names:
        current_name = name
        current_sequence.append(current_name)
        duplicated_list = names
        duplicated_list.pop(duplicated_list.index(current_name))
        index = starts_with(current_name[-1], duplicated_list)

        while index is not False:
            current_name = duplicated_list[index]
            current_sequence.append(current_name)
            duplicated_list.pop(index)
            index = starts_with(current_name[-1], duplicated_list)

        if len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence

        current_sequence = []

    return longest_sequence


if __name__ == "__main__":
    print('Longest sequence:')
    print(name_sequence('pokemon names.txt'))
