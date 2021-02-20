file = None


def new_dataset():
    with open('activity.csv', 'r') as d:
        file = d.read()

    data = file.split('\n')

    dict = {}

    for line in range(0, len(data)):
        temp = data[line].split(',')
        if line == 0:
            for heading in temp:
                if '"' in heading:
                    dict[heading.strip().split('\"')[1]] = []
                else:
                    dict[heading.strip()] = []
        else:
            dict['steps'].append(temp[0])
            dict['date'].append(temp[1].split('\"')[1])
            dict['interval'].append(temp[2])

    for index, step in enumerate(dict['steps']):
        if step == 'NA':
            dict['steps'][index] = 0

    print(dict)


if __name__ == "__main__":
    new_dataset()
