# https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/3-queue/
# multiprocessing 不可用reaturn值, 所以要用queue傳回值
import multiprocessing as mp

def job(q):
    res = 0
    for i in range(1000):
        res += i+i**2+i**3
    q.put(res) # queue


if __name__ == '__main__': # 一定要在這邊下面啟用他
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,)) # args這邊','必加, 因為他要證明他是可以疊代的
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1)
    print(res2)
    print(res1 + res2)