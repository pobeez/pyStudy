import sys

print("The command line arguments are..")

for i in sys.argv:
    print(i)

print("\n\nThe PYTHONPATH IS", sys.path, "\n")
print(sys.path)