# Given the participants' score sheet for your University Sports Day, 
#you are required to find the runner-up score. 
#You are given  scores. Store them in a list and find the score of the runner-up.
# Input Format. The first line contains n. The second line contains an array of 'n' scores


if __name__ == '__main__':
    n = int(input())
    if n>=2 and n<=10:
        arr = map(int, input().strip().split(" "))
        scorelist = list(set(arr))
        scorelist.sort(reverse = True) # sort in descending order
        print (list[1]) # 2nd heighest score is the runner-up score