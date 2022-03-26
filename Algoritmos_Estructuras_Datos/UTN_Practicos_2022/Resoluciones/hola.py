import sys

def hello(a,b):
    print ("hello my name{a} that's your sum{b}:")

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    hello(a, b)