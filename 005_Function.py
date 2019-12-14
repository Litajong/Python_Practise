import sys

def plus(x,y):
    return x + y
def minus(x,y):
    return x - y
def multiply(x,y): 
    return x * y
def divide(x,y):
    return x / y

if sys.argv[3] == 'plus':
    print('Output:', plus(int(sys.argv[1]) , int(sys.argv[2])))
elif sys.argv[3] == 'minus':
    print('Output:', minus(int(sys.argv[1]) , int(sys.argv[2])))    
elif sys.argv[3] == 'multiply':
    print('Output:', multiply(int(sys.argv[1]) , int(sys.argv[2])))
elif sys.argv[3] == 'divide':
    print('Output:', divide(int(sys.argv[1]) , int(sys.argv[2])))
    