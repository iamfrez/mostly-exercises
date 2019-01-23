def isPowerOf2(n):
    # Bitwise operator treat operands as sequences of binary digits, and operate them
    # bit by bit
    # In this case, & is bitwise AND
    return n != 0 and (int(n) & (int(n) - 1)) == 0
def counterGame(tests):
    # Write your code here
    for t in tests:
        a = int(t)
        counter = 1
        while a != 1:
            if isPowerOf2(a):
                a = a/2
            else:
                for i in range(a, -1, -1):
                    if isPowerOf2(i):
                        a = i
                        break
            counter += 1

        if counter % 2 == 0:
            print('Richard')
        else:
            print('Louise')


if __name__ == '__main__':
    tests_count = int(input().strip())

    tests = []

    for _ in range(tests_count):
        tests_item = input()
        tests.append(tests_item)

    counterGame(tests)
