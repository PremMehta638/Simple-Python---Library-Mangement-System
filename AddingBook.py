import DateTime
def add_book():
    flag = False
    while flag == False:
        print()
        print("|---------------------------------------------------|")
        print("|--------    Adding Books to the Library    --------|")
        print("|---------------------------------------------------|")

        try:
            print()
            Bookname = input("Enter Name of Book: ")
            Authorname = input(f"Enter Author Name of {Bookname}: ")
            Bookquantity = int(
                input(f"Enter Quantity of {Bookname}: "))
            Bookprice = float(input(f"Enter Price of {Bookname}: $"))

            with open("Stock.txt", "w+") as f:
                f.write(Bookname + "," + Authorname +"," + str(Bookquantity) + "," + str("$") + str(Bookprice))

            loop = True
            while loop == True:
                print()
                user= input(
                    "Do You Want To Add More Books? Press Y For Yes And N For No. : ")

                if (user.upper() == "Y"):
                    Bookname = input("Enter Name of Book: ")
                    Authorname = input(f"Enter Author's Name of {Bookname}: ")
                    Bookquantity = int(input(f"Enter Quantity of {Bookname}: "))
                    Bookprice = float(input(f"Enter Price of {Bookname}: $"))
                    

                    with open("Stock.txt", "a") as f:
                        f.write("\n" + Bookname + "," + Authorname +"," + str(Bookquantity) + "," + str("$") + str(Bookprice))
                    flag = False

                elif (user.upper() == "N"):
                    loop = False
                    flag = True

                else:
                    print()
                    print("  !!! Choose Y For Yes Or N For No")

        except ValueError:
            print()
            print("  !!! Please Input Valid Information")
            add_book()