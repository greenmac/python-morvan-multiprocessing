# https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/4-comparison/
import multiprocessing as mp
import threading as td
import time

def job(q):
    res = 0
    for i in range(1000000):
        res += i+i**2+i**3
    q.put(res) # queue

def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,)) # args這邊','必加, 因為他要證明他是可以疊代的
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:', res1 + res2)

def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i+i**2+i**3
    print('normal:', res)

def multithread():
    q = mp.Queue()
    t1 = td.Thread(target=job, args=(q,)) # args這邊','必加, 因為他要證明他是可以疊代的
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:', res1 + res2)

if __name__ == '__main__': # 一定要在這邊下面啟用他
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time:', st1-st)
    multithread()
    st2 = time.time()
    print('multithread time:', st2-st1)
    multicore()
    st3 = time.time()
    print('multicore time:', st3-st2)