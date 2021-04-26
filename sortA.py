import time
import numpy as np
from utils import dbutils

startTime = time.time()
all_data = dbutils.get_all_table()

sorted_data = all_data.sort_values(by=['Name'])
# Db2Pandas.write_column(sorted_data, "aaa")
np.savetxt(r"Sorting-step1.txt", sorted_data["Name"].array, fmt='%s')
print(f"Time taken {time.time() - startTime}")
dbutils.write_into_result(1, "Sorting-step1_Process_time", {int(time.time() - startTime)})
print("complete")
