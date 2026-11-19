scores = []

for i in range(5):
    grade = int(input("Enter score: "))
    scores.append(grade)

highest = max(scores)
lowest = min(scores)
average = sum(scores) / len(scores)

print("Scores:", scores)
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", format(average, ".2f"))
