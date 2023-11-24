import random

quiz = [["3+5","8"],["10/2","5"],["3*5","15"],["35-7","28"],["3*6","18"],["24-5","19"],["5*4","20"],["18/6","3"],["6*7","42"],["56-16","40"]]

questions = random.sample(quiz,k=10)
count = 0
for i in range(0,5):
    
    for y in range(0,4):
        if y < 3:
            print("What is the answer for : ",questions[i][0])
            user = input("Enter Answer: ")
            
            if user == questions[i][1] and y==0:
                print("Correct!!!")
                count = count + 20
                break
            elif user == questions[i][1] and y==1:
                print("Correct!!!")
                count = count + 10
                break
        
            elif user == questions[i][1] and y==2:
                print("Correct!!!")
                count = count + 5
                break
            elif user != questions[i][1] and y==0:print('\n“Wrong answer! You can try once more!”\n')
            elif user != questions[i][1] and y==1:print("\n“Wrong answer again! You can try once more!\n")
        else:
            print("\nWrong answer! No more tries allowed!\n")
            
    print("\n\n***************************************************************")

print("Your Score is ",count)
if count >= 80 and count <= 100:print("Excellent")

elif count >= 65 and count <80:print("Very Good")

elif count >= 50 and count < 65:print("Good")

elif count < 50 and coount >=0:print("Need more practice")

