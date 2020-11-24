import time

def countdown(func):
    def seconds(*args):
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        return func(*args)
    return seconds

@countdown
def time_now():
    print(time.strftime('%H:%M', time.localtime()))

print("What time is it now?")
time_now()