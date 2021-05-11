# Given an array of numbers get the average of distinct numbers

def average(array):
    tot = sum(set(array))
    length = len(set(array))
    avg = float(tot)/float(length)
    return(avg)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)