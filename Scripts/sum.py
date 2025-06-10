import sys
def sum(a,b):
    sum = int(a) + int(b)
    print("The sum is ", sum)

if __name__=="__main__":
    sys.argv[0]
    sum(sys.argv[1],sys.argv[2])
