import random

List1 = ["Jack", "rose", "Daniel", "Alexis", "Jim"]
List2 = ["Smith", "Kaipio", "Abdulla", "Smart", "Strong"]
username = []
for i in range(0,len(List1)):
    # creating random usernames
    x = random.randint(100,999)
    # creating greeting messages
    print("Dear " + (List1[i]).title()+" "+List2[i]+",")
    print('Thank you for taking part in the upcoming seminar on “Programming”. The seminar will begin 10 and will end at 16:00, followed by a complementary afternoon tea on Wednesday and Thursday this week. Registration starts at 10 am on Wednesday.')
    
    print("*** Your username is "+(List1[i][0:1]).upper()+(List2[i][0:3].upper())+ str(x)+" ***\nBest Wishes,\nSeminar Organizer")
    print("\n\n*******************************************************************************")
    
    username.append((List1[i][0:1]).upper()+(List2[i][0:3].upper())+ str(x))
     

print("\nUsernames in List 3 = ",username)
