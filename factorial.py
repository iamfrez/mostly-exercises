import math

def factorial(n):
    # Write your code here
    # res = 1
    # for i in range(1, n + 1):
    #     res = res * i
    # return res
    return math.factorial(n)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    print(str(result) + '\n')
    #fptr.write(str(result) + '\n')

    #fptr.close()
