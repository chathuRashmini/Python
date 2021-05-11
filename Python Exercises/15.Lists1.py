# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

# Initialize your list and read in the value of 'n' followed by 'n' lines of commands 
# where each command will be of the 'n' types listed above. 
# Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    N = int(input())
    numList = list()
    for i in range(N):
        cmd = input().split()
        if cmd[0] == "insert":
            pos = int(cmd[1])
            val = int(cmd[2])
            numList.insert(pos, val)
        elif cmd[0] == "append":
            val = int(cmd[1])
            numList.append(val)
        elif cmd[0] == "remove":
            val = int(cmd[1])
            numList.remove(val)
        elif cmd[0] == "print":
            print(numList)
        elif cmd[0] == "pop":
            numList.pop()
        elif cmd[0] == "sort":
            numList.sort()
        elif cmd[0] == "reverse":
            numList.reverse()