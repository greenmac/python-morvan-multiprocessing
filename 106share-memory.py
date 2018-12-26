# https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/6-shared-memory/
import multiprocessing as mp

value = mp.Value('d', 1)
array = mp.Array('i', [1, 3, 3])