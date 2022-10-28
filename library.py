class Library:
    def __init__(self, libraryname, bookname):
        self.libraryname = libraryname
        self.bookname = bookname
        Library.log(self)

    def __str__(self):
        return self.bookname

    @staticmethod
    def gatedate():
        """ time stamp"""
        import datetime
        return datetime.datetime.now()

    @staticmethod
    def getList(dict):
        return list(dict.keys())

    booklog = {}

    def log(self):
        with open(f"{self.libraryname}.txt", "a") as f:
            for i in range(len(self.bookname)):
                f.write(f"{self.bookname[i]} : {Library.gatedate()}\n")

    def lendbook(self):
        name = input("Enter your name:\t").upper()
        while True:
            bookname1 = input("Enter the name of the book.:\t").upper()
            if bookname1 in Library.booklog:
                Library.availablebook(self)
            else:
                if bookname1 in self.bookname:
                    Library.booklog.update({f"{bookname1}": f"Book lend at {Library.gatedate()} by {name}"})
                    with open(f"{self.libraryname}.txt", "a") as f:
                        f.write(f"{bookname1} : {name} : Lending date - {Library.gatedate()}\n")
                    return print(f"{bookname1}(Book lending date)", " : ", f"{Library.booklog[bookname1]}")
                else:
                    print(f"The name of the book is{self.bookname}")

    def returnbook(self):
        name = input("Enter your name:\t").upper()
        while True:
            bookname1 = input("Enter the name of the book.:\t").upper()
            if bookname1 in Library.booklog:
                Library.booklog.pop(f"{bookname1}")
                with open(f"{self.libraryname}.txt", "a") as f:
                    f.write(f"{bookname1} : {name} : Return date - {Library.gatedate()}\n")
                return print(f"{bookname1}  : Book return at {Library.gatedate()} by {name}")
            else:
                print(f"The name of the book is{self.bookname}")

    def availablebook(self):
        bookname2 = self.bookname.copy()
        a = Library.getList(Library.booklog)
        for i in range(len(a)):
            bookname2.remove(a[i])
        return print(f"Available books are : {bookname2}")

    def add(self):
        while True:
            book = input("Enter name of book:\t").upper()
            print("Type 'exit()' after all the entry")
            self.bookname.append(book)
            if book == "EXIT()":
                self.bookname.remove("EXIT()")
                return self.bookname
            else:
                with open(f"{self.libraryname}.txt", "a") as f:
                    f.write(f"{book} : {Library.gatedate()}\n")

import  time

libraryname = input("Enter the name of the library:\t").upper()
book = [input("Enter name of book 1:\t").upper(), input("Enter name of book 2:\t").upper(), input("Enter name of book 3:\t").upper()]
newlibrary = Library(libraryname, book)
while True:
    print(newlibrary.bookname)
    time.sleep(3)
    print("press B to see available book in the library\n"
          "Press L for leding.\n"
          "Press R for return.\n"
          "Press A for adding.\n"
          "Type 'end' to end the progrm")
    choice = input("Enter your choice:\t").lower()
    if choice == 'l':
        newlibrary.lendbook()
        time.sleep(3)
    elif choice == 'r':
        newlibrary.returnbook()
        time.sleep(3)
    elif choice == 'a':
        newlibrary.add()
        time.sleep(3)
    elif choice == 'b':
        newlibrary.availablebook()
        time.sleep(3)
    elif choice == 'end':
        break