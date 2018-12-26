# https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/5-pool/
import multiprocessing as mp

def job(x):
    return x*x

def muticore():
    pool = mp.Pool(processes=2) # processes設定用幾個核, 沒設就是全部平均
    res = pool.map(job, range(10))
    print(res)
    # res = pool.apply_async(job, (2, 2, 3, 4,))
    # print(res.get())
    muiti_res = [pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in muiti_res])

if __name__ == '__main__':
    muticore()
