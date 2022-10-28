def gatedate():
    """ time stamp"""
    import datetime
    return datetime.datetime.now()


def log():
    """to log in new log"""
    b = name1()
    c = chart1()
    if c == 'food':
        n = str(input("enter what you want to log:\n"))
        with open(f"{b}_food.txt",'a') as f:
            f.write(str(gatedate()))
            f.write("   :   ")
            f.write(f"{n}\n")
            print(str(gatedate()),end="")
            print(" :   "+n)
        program()
    elif c == 'exercise':
        n = str(input("enter what you want to log:\n"))
        with open(f"{b}_exercise.txt",'a') as f:
            f.write(str(gatedate()))
            f.write("   :   ")
            f.write(f"{n}\n")
            print(str(gatedate()), end="")
            print(" :   "+n)
        program()

def recall():
    """to reacall old log"""
    b = name1()
    c = chart1()
    if c == 'food':
        with open(f"{b}_food.txt") as f:
            p = f.read()
            print(p)
        program()
    elif c == 'exercise':
        with open(f"{b}_exercise.txt") as f:
            p = f.read()
            print(p)
        program()



def logic():
    """logic of the health manage ment system"""
    t = input("what you want to do{log(l)/recall(r)}:\t").lower()
    if t == 'r':
        return recall()
    elif t == 'l':
        return log()
    else:
        print("choose l or r only")
        return logic()


def name1():
    """to restrict the name in this three"""
    name = input("Enter the member name(larry/rohan/hamad):\t").lower()
    if name == 'rohan' or name=='larry' or name=='hamad':
        return name
    else:
        print("choose between this larry/rohan/ hamad")
        return name1()

def chart1():
    """keep the chart between this two"""
    chart = input("Enter which one you want(food/exercise):\t").lower()
    if chart == 'food' or chart == 'exercise':
        return chart
    else:
        print("choose food or exercise only")
        return chart1()

def program():
    a = input("you wnat to continue?(Y/N) :\t").lower()
    if a == 'y':
        return logic()
    elif a == 'n':
        return None
    else:
        print("only press y or n")
        return program()


logic()