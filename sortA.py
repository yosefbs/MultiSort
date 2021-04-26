import time
import numpy as np
from utils import Db2Pandas

startTime = time.time()
all_data = Db2Pandas.get_all_table()

sorted_data = all_data.sort_values(by=['Name'])
#Db2Pandas.write_column(sorted_data, "aaa")
np.savetxt(r"res1.txt", sorted_data["Name"].array, fmt='%s')
print(f"Time taken {time.time() - startTime}")
print("complete")
