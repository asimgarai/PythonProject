class Guess_number:
    @staticmethod
    def guess():
        username = input("Enter your name:\n").upper()
        import random
        randomnNo = random.randint(1, 100)
        for i in range(1, 6):
            n = int(input("Enter your guess:\t"))
            if randomnNo == n:
                print("********** CONGRATULATION YOU FIND IT **********")
                print(f"You take {i} chance ")
                with open("Score.txt","a") as f:
                    f.write(f"{username} take {i} chance.\n")
                Guess_number.program()
                break
            elif (n < randomnNo, n > randomnNo):
                print(f"You have left {5 - i} guess")
                while randomnNo < n:
                    if randomnNo < n < (randomnNo + 10):
                        print("Thora or kam\n")
                        break
                    else:
                        print("Kam karo\n")
                    break
                while randomnNo > n:
                    if randomnNo > n > (randomnNo - 10):
                        print("Thora or jayada\n")
                        break
                    else:
                        print("Jayada karo\n")
                    break
        else:
            print("G A M E       O V E R")
            print(f"The number is {randomnNo}")
            with open("Score.txt", "a") as f:
                f.write(f"{username} loss after using all the chance.\n")
            Guess_number.program()
    @staticmethod
    def program():
        a = input("you wnat to continue?(Y/N) :\t").lower()
        if a == 'y':
            return Guess_number.guess()
        elif a == 'n':
            return None
        else:
            print("only press y or n")
            return Guess_number.program()


game = Guess_number()
game.guess()
