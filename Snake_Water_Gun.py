import random
def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False
list = ['s', 'w', 'g']                       #it can also be used
# randNo = random.randint(1,3)
# if randNo==1:
#     comp = "s"
# if randNo==2:
#     comp = "s"
# if randNo==3:
#     comp = "g"
list1=[]
i = 0
while i<11:
    comp = random.choice(list)
    print("comp turn: Snake(s) Water(w) Gun(g)?")
    you = input("Your turn: Snake(s) Water(w) Gun(g)?):\t")
    while you != 's' and you != 'g' and you != 'w':
        print("Enter wrong input!")
        you = input("Please enter again:\t")
    a = gamewin(comp, you)
    print(f"Comp choose {comp} and you choose {you}")
    if a == True:
        list1.append("you win!")
        print("you win!")
    elif a == False:
        list1.append("You loose!")
        print("You loose!")
    elif a == None:
        print("Its a Tie")
    i = i+1
s = list1.count("you win!")
w = list1.count("You loose!")
print(f"you win {s} times and computer win {w} times")
if s>w:
    print("You win the match!")
elif s<w:
    print("You loss the match!")
else:
    print("its a tie!")