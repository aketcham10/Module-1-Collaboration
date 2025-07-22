# Module 6
# Zane Ketcham
# Concurrency

import datetime
# 13.1
def today():
    # write the current date to a text file named today.txt
    with open('today.txt', 'w') as f:
        f.write(str(datetime.date.today()))

# 13.2
def read_today():
    # read the current date from a text file named today.txt
    with open('today.txt', 'r') as f:
        today_string = f.read()
    return today_string

# 13.3
def parse_date(date_string):
    return datetime.datetime.strptime(date_string, '%Y-%m-%d').date()

if __name__ == '__main__':
    today()
    today_string = read_today()
    print(parse_date(today_string))


