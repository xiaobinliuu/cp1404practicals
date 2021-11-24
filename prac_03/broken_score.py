def main(): #this will give the score and show if the score is bad, passable or excellent
    score = float(input("enter score: "))
    print(score_is(score))

def score_is(score): #shows if the score is bad, passable or excellent
    if score  < 0 or score > 100:
        print("invalid score")
    elif score >= 90 <= 100:
        print("excellent")
    elif score >= 50:
        print("pass")
    else:
        print("bad")

main()