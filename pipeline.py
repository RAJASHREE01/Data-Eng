import pandas as pd
import sys

print(sys.argv)

day = sys.argv[1]
#first [0] parameter will be the file name
#then [1] and so on are the passed parameters

print(f"successful for today: {day}")