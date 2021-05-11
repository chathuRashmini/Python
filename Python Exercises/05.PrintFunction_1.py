# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following:
# 123...n
# ex: n = 5 -> output: 12345

if __name__ == '__main__':
    n = int(input())
    if n>=1 and n<=150:
        print(*range(1, n+1), sep='')