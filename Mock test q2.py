import random

quiz = [["3+5","8"],["10/2","5"],["3*5","15"],["35-7","28"],["3*6","18"],["24-5","19"],["5*4","20"],["18/6","3"],["6*7","42"],["56-16","40"]]
#print(len(quiz))
questions = random.sample(quiz,k=10)
count = 0
for i in range(0,5):
    print("What is the answer for : ",questions[i][0])
    user = input("Enter Answer: ")
    if user == questions[i][1]:
        print("Correct!!!")
        count = count + 1
        
    else:print("Incorecct!!!\nCorrect Answer is ",questions[i][1])

    print("\n\n***************************************************************")

print("Your Score is ",count)
if count <= 5 and count >=4: print("Excellent")
elif count == 3:print("not bad")
elif count <= 2 and count >=0:print("Need more practice")
