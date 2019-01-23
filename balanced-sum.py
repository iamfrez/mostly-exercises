def balancedSum(sales):
    # Write your code here
    index = -1
    for i in range(len(sales)):
        #print('{} - {} - {}'.format(sum(sales[:i]), i, sum(sales[i + 1:])))
        if sum(sales[:i]) == sum(sales[i + 1:]):
            index = i
    return index

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sales_count = int(input().strip())

    sales = []

    for _ in range(sales_count):
        sales_item = int(input().strip())
        sales.append(sales_item)

    result = balancedSum(sales)
    print(str(result) + '\n')
#    fptr.write(str(result) + '\n')

#    fptr.close()
