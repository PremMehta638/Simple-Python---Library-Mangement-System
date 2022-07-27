import DateTime
import List


def BorrowBook():
    flag = False
    while flag == False:
        print("Choose the Book given below: ")
        print()
        for i in range(len(List.BookName)):
            print("\tEnter", i, "to borrow a book", List.BookName[i])

        try:
            print()
            a = int(input("My Choice is: "))
            try:
                if(int(List.Quantity[a]) > 0):

                    print("Book is available")

                    while (True):
                        FirstName = input("Enter the First Name: ")
                        if FirstName.isalpha():
                            break
                        print("Please provide Proper Name")
                    while(True):
                        LastName = input("Enter the Last Name:  ")
                        if LastName.isalpha():
                            break
                        print("Please provide Proper Name")

                    text = "Borrow---"+FirstName+".txt"
                    # Creating a file which record the borrower details

                    with open(text, "w+") as link:
                        link.write(
                            "----------Library Management System------------\n")
                        link.write("                     \n")
                        link.write("     ----Details of Borrower----")
                        link.write("Borrowed By: "+FirstName+" "+LastName+"\n")
                        link.write("   Date: "+DateTime.getDate() +
                                   "     Time:"+DateTime.getTime()+"\n")
                        link.write(
                            "S.N. \t\t BookName \t         AuthorName \n")

                    with open(text, "a") as f:
                        f.write(
                            "1. \t\t"+List.BookName[a]+"\t\t "+List.AuthorName[a]+"\n")

                    cost = List.BookCost[a]
                    
                    #Decreasing the quantity of selected book
                    List.Quantity[a] = int(List.Quantity[a])-1
                    #Updating the Stock file after decrement
                    with open("Stock.txt", "w+") as f:
                        for i in range(len(List.BookName)):
                            f.write(List.BookName[i]+","+List.AuthorName[i] +
                                    ","+str(List.Quantity[i])+"," + "$" + List.BookCost[i]+"\n")

                    # Code for borrowing for multiple book
                    loop = True
                    total = 1  # for adding multiple book
                    while loop == True:
                        print()
                        selection = input(
                            FirstName+" Do you want to Borrow more Books? But You can't borrow same book twice. Input Y for yes and N for no.")
                        if(selection.upper() == "Y"):
                            total += 1
                            print("Please choose an option below")
                            print()

                            # iterating the book name to display available books
                            for i in range(len(List.BookName)):
                                print("\tEnter", i, "to borrow a book",
                                      List.BookName[i])
                            print()
                            a = int(input("My Choice is: "))  # asking choice
                            if(int(List.Quantity[a]) > 0):
                                print("Requested Book is Available")
                                with open(text, "a") as f:
                                    f.write(
                                        str(total)+".""\t\t"+List.BookName[a]+"\t\t  "+List.AuthorName[a]+"\n")

                            #    Storing the price of the book
                                # price=0
                                # cost = float(price) + \
                                #     float(List.BookCost[a])

                                # decreasing the Quantity of book
                                List.Quantity[a] = int(List.Quantity[a])-1

                                # updating the stock file where quantity of book decrease
                                with open("Stock.txt", "w+") as improve:
                                    for i in range(len(List.BookName)):
                                        improve.write(List.BookName[i]+","+List.AuthorName[i] +
                                                      ","+str(List.Quantity[i])+"," + "$" + List.BookCost[i]+"\n")
                                    flag == False

                            else:
                                loop == False
                                break

                        elif(selection.upper() == "N"):
                            print()
                            print("!!!Thank You For Borrowing Book From us.")
                            print()
                            with open(text, "a")as cost:
                                cost.write(
                                    "\n Total Borrow Price: $" + str(cost))
                            with open(text, "r") as read:
                                display = read.read()
                                print(display)
                            loop = False
                            flag = True
                        else:
                            print("Please choose as instructed")

                else:
                    print("Sorry!!! the selected Book is not available at this moment. Please come back later")

            except IndexError:
                print("")
                print("Please choose book according to their number.")
        except ValueError:
            print("")
            print("Please selcect accordingly.")