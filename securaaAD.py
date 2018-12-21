import subprocess
import time

cmd = "cd C:\\CodeRepository\zona_services\zona_ad & git pull"
returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
print('returned value:', returned_value)
print("sleeping for 60 sec, pulling from git")
time.sleep(60)


cmd1 = "go clean"
returned_value1 = subprocess.call(cmd1, shell=True)
print('returned value:', returned_value1)
print("sleeping for 10 sec, GO clean executing")
time.sleep(10)


cmd2 = "go build"
returned_value2 = subprocess.call(cmd2, shell=True)
print('returned value:', returned_value)
time.sleep(50)
