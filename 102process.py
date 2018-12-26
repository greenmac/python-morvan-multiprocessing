# https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/2-add/
import multiprocessing as mp

def job(a, b):
    print('aaaaa')

if __name__ == '__main__': # 一定要在這邊下面啟用他
    p1 = mp.Process(target=job, args=(1, 2))
    p1.start()
    p1.join()