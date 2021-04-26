import sys
import time

from sortBase import *
import multiprocessing as mp

if __name__ == "__main__":
    from_db_to_sorted_file(int(sys.argv[1]), sys.argv[2], sys.argv[3])
