# Given the names and grades for each student in a class of 'n' students, 
# store them in a nested list and print the name(s) of any student(s) 
# having the "second lowest grades" in "alphabetical order"
# Ex:
# input:
# 3
# Edward
# 50
# Bella
# 43
# Alice
# 31
# Jacob
# 43
# output:
# Bella
# Jacob

if __name__ == '__main__':
    scorelist = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scorelist[name] = score
    sortedScores = sorted(scorelist.values())
    s = sortedScores[0];
    for score in sortedScores:
    	if score != s:
    		secondLowest = score
    		break
    
    names = list()
    for key, value in scorelist.items():
        if value == secondLowest:
            names.append(key)
    names.sort()
    for name in names:
        print(name)