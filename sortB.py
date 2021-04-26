import time

from sortBase import *


def sort2():
    for i in range(0, chunks):
        start = chunk_size * i
        end = start + chunk_size
        from_db_to_sorted_file(start+1, end, rf'chunk_{i}.txt')


if __name__ == "__main__":
    startTime = time.time()
    sort2()
    merge_files("Sorting-step2.txt")
    print(f"Time taken {time.time() - startTime}")
    dbutils.write_into_result(1, "Sorting-step2_Process_time", int(time.time() - startTime))
    print("complete")
