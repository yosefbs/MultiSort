import sys
import time

from sortBase import *
import multiprocessing as mp


if __name__ == "__main__":

    pool = mp.Pool(mp.cpu_count())
    startTime = time.time()
    data = range(0, chunks)
    results = [pool.apply(from_db_to_sorted_file, args=(chunk_size * i + 1,chunk_size * (i + 1) , rf'chunk_{i}.txt')) for i in data]
    pool.close()
    merge_files("res3.txt")
    print(f"Time taken {time.time() - startTime}")


