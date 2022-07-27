import BookBorrow
import DateTime
import List
import BookReturn
import AddingBook

def HereWeGo():
    while(True):
        print()
        print()
        print("|---------------------------------------------------------|")
        print("|--------        Welcome to Central Library        -------|")
        print("|--------       Itahari International college     --------|")
        print("|---------------------------------------------------------|")
        print("")
        print("")
        print("")
        print("     Enter 1. To Add Book")
        print("     Enter 2. To Display ")
        print("     Enter 3. To Borrow a book")
        print("     Enter 4. To Return a book")
        print("     Enter 5. To exit")

        try:
            print()
            print()
            Choice=int(input("Please select a Choice from 1-4 for futher processing: "))
            print()
            if(Choice==1):
                print()
                print()
                AddingBook.add_book()
            
            elif(Choice==2):
                print()
                print()
                print("|-----------Available Books are---------|")
                print("|---------------------------------------|")
                print()
                with open("Stock.txt","r") as f:
                    lines=f.read()
                    print(lines)

            elif(Choice==3):
                List.listOfBooks()
                BookBorrow.BorrowBook()

            elif(Choice==4):
                List.listOfBooks()
                BookReturn.book_return()

            elif(Choice==5):
                print("Thank You!!! For Using the Library Management System")
                print("|------    Please Visit us again    ------|")
                print("|-------------Have a Nice Day------------|")
                break
            
            else:
                print("Please kindly Select a choice in between 1-4 which are provided to You")
        except ValueError:
            print("You are requested to input the provided value. Thank You!!!")
HereWeGo()
