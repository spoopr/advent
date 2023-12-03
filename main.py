import os, threading, sys

base_dir = os.getcwd()

with open("run.txt","r+") as file:
  a = file.read()
  print(f"\nrunning {a}/solution.py\n")
  os.chdir(base_dir+"/" +a)
  try:
    os.system("python3 solution.py")
  except KeyboardInterrupt:
    pass
print("completed")