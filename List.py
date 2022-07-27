def listOfBooks():

    global BookName
    global AuthorName
    global Quantity
    global BookCost

    BookName = []
    AuthorName = []
    Quantity = []
    BookCost = []

    with open("Stock.txt", "r") as f:
        lines = f.readlines()
        Empty_list = []

        for z in lines:
            remove = z.strip('\n')
            Empty_list.append(remove)
        for i in range(len(Empty_list)):
            book_list = Empty_list[i].split(',')
            value = 0
            for b in book_list:
                if(value == 0):
                    BookName.append(b)
                elif(value == 1):
                    AuthorName.append(b)
                elif(value == 2):
                    Quantity.append(b)
                elif(value == 3):
                    BookCost.append(b)
                value += 1


listOfBooks()
