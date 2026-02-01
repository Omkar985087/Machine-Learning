import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"number:{i}")

def print_letters():
    for i in "abcde":
        time.sleep(2)
        print(f"letter:{i}")

p1=threading.Thread(target=print_numbers)
p2=threading.Thread(target=print_letters)

t=time.time()
p1.start()
p2.start()

p1.join()
p2.join()

finished_time=time.time()-t
print(finished_time)
