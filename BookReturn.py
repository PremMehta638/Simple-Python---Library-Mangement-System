import DateTime
import List


def book_return():
    List.listOfBooks()
    print()
    Name = input("Enter the Name of the Borrower: ")
    file = "Borrow by-"+Name+".txt"

    try:
        with open(file, "r") as read:
            Borrower_Details = read.read()
            print(Borrower_Details)

        doc = "Return---"+Name+".txt"
        with open(doc, "r") as info:
            info.write("                Library Management System \n")
            info.write("                   Returned By: " + Name+"\n")
            info.write("    Date: " + DateTime.getDate() +
                       "    Time:" + DateTime.getTime()+"\n\n")
            info.write("S.N.\t\tBookname\t\tCost\n")

        with open(doc, "r") as f:
            lines = f.readlines()
            empty_list = []

            for z in lines:
                # creating an empty list to remove "\n"
                clear = z.strip('\n')
                # appending the list after removing "\n"
                empty_list.append(clear)

        total = 1
        cost = 0.0
        for i in range(len(List.BookName)):

            if List.BookName[i] in Borrower_Details:
                with open(doc, "a") as info:
                    info.write(
                        "\n " + str(total) + " " + List.BookName[i]+"   " + "$" + List.BookCost[i])
                    total += 1

                cost = float(cost) + float(List.BookCost[i])

                # increasing the selected book quantity
                List.Quantity[i] = int(List.Quantity[i])+1
                # updating the stock file
                with open("Stock.txt", "w+") as info:
                    for i in range(len(List.BookName)):
                        info.write(List.BookName[i]+","+List.AuthorName[i]+","+str(
                            List.Quantity[i]+"," + "$" + List.BookCost[i]+"\n"))
        with open(doc, "a") as update:
            update.write(
                "\n             Total Cost of Borrow:$" + str(cost)
            )
        CostWithFine = 0.0
        success = False
        while success == False:
            print()
            print()
            print("Is the Book return date expired?")
            ask = input("Press Y for Yes and N for No")
            if(ask.upper() == "Y"):

                print("By How many days was the book returned late ?")
                print()
                day = int(input("Total days: "))

                CostWithFine = float(cost) + float(day*1.5)

                with open(doc, 'a') as Newcost:
                    Newcost.write(
                        "\n                    Total Fine: $ "
                    )
                    Newcost.write(
                        "\n                     Total Cost with Fine: $" +
                        str(CostWithFine)
                    )
                with open(doc, "r") as F:
                    display = f.read()
                    print(display)
                    success = True
            elif(ask.upper() == "N"):
                print()
                with open(doc, "a") as Newcost:
                    Newcost.write(
                        "\n                     Total Return Price: $" +
                        str(cost)
                    )
                with open(doc, "r")as info:
                    display = info.read()
                    print(display)
                    success = True
            else:
                print("!!!Please provide correct input")
    except:
        print("!!!You Haven't Borrowed any books")
        book_return()
