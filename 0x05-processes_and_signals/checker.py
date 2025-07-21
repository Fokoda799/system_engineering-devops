#!/usr/bin/env python3
"""
Validate
"""
import subprocess
from subprocess import DEVNULL
import time


def pid_process(process_name):
    ps_outputs=subprocess.Popen(["ps", "-ax"], stdout=subprocess.PIPE).communicate()[0].decode('utf-8').split("\n")
    pid = None
    for ps_line in ps_outputs:
        ps_line = ps_line.lstrip()
        if process_name in ps_line:
            pid = ps_line.split(" ")[0]
            break
    return pid


# start 7-highlander
subprocess.Popen(["./7-highlander"], stdout=DEVNULL, stderr=DEVNULL)
# wait 5 sec
time.sleep(5)

# check if process running
pid_highlander = pid_process("7-highlander")

if pid_highlander is None:
    print("7-highlander not running")
    exit(-1)

# try to kill 7-highlander
subprocess.Popen(["./8-beheaded_process"])

time.sleep(5)

# Check if  7-highlander is dead
pid_highlander2 = pid_process("7-highlander")

# stop 7-highlander
#subprocess.Popen(["kill", "-9", pid_highlander])

if pid_highlander2 is not None:
    print("./7-highlander is still running")
    exit(-1)
print("OK", end="")
