import calendar


def gen_calendar(temp_month, temp_year):
    return calendar.month(temp_year, temp_month, 0, 1)


if __name__ == "__main__":
    month = int(input("Month: "))
    year = int(input("Year: "))
    print(gen_calendar(month, year))
