import statistics


file = None


def stats(filename):
    with open(filename, 'r') as d:
        file = d.read()

    data = file.split('\n')

    dates_steps = {}
    steps_per_day = []

    for line in range(0, len(data)):
        temp = data[line].split(',')
        if line == 0:
            pass
        else:
            dates_steps.setdefault(temp[1])

    step_total = 0

    for line in range(0, len(data)):
        temp = data[line].split(',')
        if line == 0:
            pass
        else:
            if temp[2] != '2355':
                if temp[0] == 'NA':
                    pass
                else:
                    step = int(temp[0])
                    step_total += step
            elif temp[2] == '2355':
                if temp[0] == 'NA':
                    steps_per_day.append(temp[0])
                else:
                    step = int(temp[0])
                    step_total += step
                    steps_per_day.append(step_total)
                    step_total = 0

    for i in range(0, len(dates_steps)):
        dates_steps[list(dates_steps)[i]] = steps_per_day[i]

    steps_per_day_no_str = []
    for step in steps_per_day:
        if step == 'NA':
            pass
        else:
            steps_per_day_no_str.append(step)

    median_steps = statistics.median(steps_per_day_no_str)
    mean_steps = int(statistics.mean(steps_per_day_no_str))

    total_missing = 0
    for line in range(0, len(data)):
        temp = data[line].split(',')
        if line == 0:
            pass
        else:
            if temp[0] == 'NA':
                total_missing += 1

    print("Steps per day:", '\n', dates_steps)
    print('\nMedian:', median_steps)
    print('Mean:', mean_steps)
    print('Total missing values:', total_missing)


if __name__ == "__main__":
    stats('activity.csv')
