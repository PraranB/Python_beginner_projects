print("WELCOME!!!")
quiz = input("What to Solve Quiz ? ")
if quiz.lower() != "yes":
    quit()

print("Let's Play!! :D")
Score = 0

ans = input("Q1. Which Planet is closest to sun? ").lower()
if ans == 'mercury' :
    print("Correct \n+1 point")
    Score +=1
else:
    print("Incorrect")

ans = input("Q2. What is the term for a natural satellite? ").lower()
if ans == 'moon' :
    print("Correct \n+1 point")
    Score +=1
else:
    print("Incorrect")

ans = input("Q3. What is the name of the force which keeps the planets in orbit around the sun? ").lower()
if ans == 'gravity' :
    print("Correct \n+1 point")
    Score +=1
else:
    print("Incorrect")

ans = input("Q4. Which planet is covered by clouds of sulphuric acid? ").lower()
if ans == 'venus' :
    print("Correct \n+1 point")
    Score +=1
else:
    print("Incorrect")

ans = input("Q5. What shape is the Milky Way? ").lower()
if ans == 'spiral' :
    print("Correct \n+1 point")
    Score +=1
else:
    print("Incorrect")

print("Your Score is " +str(Score) + ".")