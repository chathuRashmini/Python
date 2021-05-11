def split_and_join(line):
    splittedline = line.split()
    joinedline = "-".join(splittedline)
    return (joinedline)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)