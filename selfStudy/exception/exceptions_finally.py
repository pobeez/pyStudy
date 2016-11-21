import sys
import time

f = None
try:
    f = open(r"..\io\poem.txt", 'r')
    while True:
        line = f.readline()
        if len(line) ==0:
            break
        print(line)
        sys.stdout.flush()
        time.sleep(1)
except IOError:
    print("Could not find poem.txt")
finally:
    if f:
        f.close()
    print("Cleanig up close poem.txt")