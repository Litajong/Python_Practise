import sys

if sys.argv[3] == "plus":
    print("Output:", int(sys.argv[1]) + int(sys.argv[2]))
if sys.argv[3] == "minus":
    print("Output:", int(sys.argv[1]) - int(sys.argv[2]))
if sys.argv[3] == "multiply":
    print("Output:", int(sys.argv[1]) * int(sys.argv[2]))    
if sys.argv[3] == "divide":
    print("Output:", int(sys.argv[1]) / int(sys.argv[2]))    