import threading
import time

# def longSquare(num):
#     time.sleep(1)
#     return num**2
#
# [longSquare(n) for n in range(0, 5)]


def longSquare(num, results):
    time.sleep(1)
    results[num] = num**2

results = {}
t1 = threading.Thread(target=longSquare, args=(1,results))
t2 = threading.Thread(target=longSquare, args=(2,results))

t1.start()
t2.start()

t1.join()
t2.join()

print(results)

#   Inefficient with declaring each threading variable
#   Better to put into a list

def longSquare(num, results):
    time.sleep(1)
    results[num] = num**2

results = {}
threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range(0, 100)]
[t.start() for t in threads]
[t.join() for t in threads]
print(results)
