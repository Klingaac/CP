n = int(input())

problems_solved = 0
for i in range(n):
    s = input()
    
    friends_sure = 0
    for j in range(0, 5, 2):
        if s[j] == "1":
            friends_sure += 1
        
        if friends_sure >= 2:
            problems_solved += 1
            break

print(problems_solved)