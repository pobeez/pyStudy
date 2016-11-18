import os
import time

source = ["c:\\py_test\\source"]
target_dir = "c:\\py_test\\target"

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

target = today + os.sep + now + ".zip"

print(target,)

if not (os.path.exists(today)):
    os.mkdir(today)
    print(today, "directory is created!!!")

zip_command = "zip -r {0} {1}".format(target, ' '.join(source))

print("Zip command is")
print(zip_command)
print("Running..")

if os.system(zip_command) == 0:
    print("Successful backup to", target)
else:
    print("Backup Failed")





