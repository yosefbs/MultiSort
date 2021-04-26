import os
import time

from sortBase import *
import subprocess
import sys

startTime = time.time()
pids = []
for i in range(0, chunks):
    start = chunk_size * i
    end = start + chunk_size
    pid = subprocess.Popen([sys.executable, "sortC.py", f"{start + 1}", f"{end}", f"chunk_{i}.txt"])  # Call subprocess
    pids.append(pid)

exit_codes = [p.wait() for p in pids]
merge_files("Sorting-step3.txt")
print(f"Time taken {time.time() - startTime}")
dbutils.write_into_result(1, "Sorting-step2_Process_time", {int(time.time() - startTime)})
