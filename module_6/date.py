# Module 6
# Zane Ketcham
# Concurrency

# 13.1

import datetime

def today():
    # write the current date to a text file named today.txt
    with open('today.txt', 'w') as f:
        f.write(str(datetime.date.today()))


