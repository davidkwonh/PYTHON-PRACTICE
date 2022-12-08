from multiprocessing import Process
import time
import threading


#   on some OS cannot use functions if function is in the same file
#   solve this issue by installing multiprocess

#   Processes do not share memory unlike threads
#   copy of dictionary in separate data space



def longSquare(num, results):
    time.sleep(1)
    print(num**2)
    print('Finished computing!')

results = {}
processes = [Process(target=longSquare, args=(n,results)) for n in range(0, 10)]
[p.start() for p in processes]
[p.join() for p in processes]


#   OUTPUT, NOTICE NEW LINES ARE F*CKED

# 01
# 4
# 9
# Finished computing!Finished computing!16
# 25Finished computing!
#
#
# 36Finished computing!
#
# 49Finished computing!64
#
# 81Finished computing!
# Finished computing!
#
#
#
# Finished computing!Finished computing!
# Finished computing!
#
#
# [None, None, None, None, None, None, None, None, None, None]


results = {}
threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range(0, 10)]
[t.start() for t in threads]
[t.join() for t in threads]
print(results)


#   Output, A lot cleaner btw

# 9163625496481
# Finished computing!
# 14
#
# Finished computing!
#
# Finished computing!
# Finished computing!
#
#
#
# Finished computing!
# Finished computing!
# 0Finished computing!
# Finished computing!
#
#
# Finished computing!
# Finished computing!
#
# {}


#   ULTIMATELY THREADING EMULATES PARALLEL COMPUTING
#   USEFUL WHEN PROGRAMS HAVE PERIODS OF DOWNTIME
#   THREADS SHARE SPACE IN MEMORY
