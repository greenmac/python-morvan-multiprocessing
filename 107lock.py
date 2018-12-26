# https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/7-lock/
import multiprocessing as mp
import time

def job(v, num, l):
    l.acquire()
    for _ in range(10):
        time.sleep(0.1) # 暂停0.1秒，让输出效果更明显
        v.value += num # v.value获取共享变量值
        print(v.value, end="/")
    l.release()
        
def multicore():
    l = mp.Lock()
    v = mp.Value('i', 0) # 定义共享变量
    p1 = mp.Process(target=job, args=(v, 1, l))
    p2 = mp.Process(target=job, args=(v, 3, l)) # 设定不同的number看如何抢夺内存
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
if __name__ == '__main__':
    multicore()