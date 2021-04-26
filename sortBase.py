import numpy as np

import Provider
from utils import dbutils
from utils.FileHandler import FileHandler

chunk_size = Provider.conf.get("ads.chunk-size")
total = Provider.conf.get("ads.total") + 1
chunks = int(total / chunk_size)


def from_db_to_sorted_file(start,end, res_file):
    # print(f"load names between ${start} - ${end}. save sorted in ${res_file}")
    sorted_data = \
        dbutils.get_partial_table_by_range(start, end) \
            .sort_values(by=['Name'])
    np.savetxt(res_file, sorted_data["Name"].array, fmt='%s')


def merge_files(res_file_name):
    import bisect
    sorted_files_list = []
    for i in range(0, chunks):
        file_name = f'chunk_{i}.txt'
        wrapped_file = FileHandler(file_name)
        bisect.insort(sorted_files_list, wrapped_file)
    res_file = open(res_file_name, 'w')
    while len(sorted_files_list) > 0:
        min_line_file = sorted_files_list.pop(0)
        line = min_line_file.get_line_and_go_next()
        res_file.write(line)
        if not min_line_file.EOF:
            bisect.insort(sorted_files_list, min_line_file)

