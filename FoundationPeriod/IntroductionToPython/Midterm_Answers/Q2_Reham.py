import random
suser_inp=input("enter r or p or s: ").split()
list_rand=['r','p','s']
choice=random.choice(list_rand)
#print(choice)
#print(suser_inp)
if (choice == "r" and suser_inp == ['s']) or (choice=='s' and suser_inp == ['p'])or (choice=='p' and suser_inp ==['r']):
    # rock beat scissors
    print("Computer wins")
elif (choice == 'r' and suser_inp == ['p']) or (choice =='p' and suser_inp == ['s'])or(choice =='s' and suser_inp == ['r']) :
    # paper beats rock
    print("User wins")
else:
    print("Tie")



