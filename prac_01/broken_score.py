

score = float(input("enter score: "))
if score  < 0 or score > 100:
    print("invalid score")
elif score >= 90 <= 100:
    print("excellent")
elif score >= 50:
    print("pass")
else:
    print("bad")
