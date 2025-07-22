import multiprocessing

# Create 3 processes and have each one wait a random number of seconds between 0 and 1, print the current time, and then exit

def worker():
    import time
    import random
    time.sleep(random.random())
    print(time.ctime())
    return

if __name__ == "__main__":
    for i in range(3):
        p = multiprocessing.Process(target=worker)
        p.start()