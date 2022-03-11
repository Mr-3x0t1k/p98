def swapFileData():
    fileName1 = input("enter the name of file 1: ")
    fileName2 = input("enter the name of file 2: ")
    with open(fileName1, 'r') as a:
        data_a = a.read()
    with open(fileName2, 'r') as b:
        data_b = b.read()
    with open(fileName1, 'w') as a:
        a.write(data_b)
    with open(fileName2, 'w') as b:
        b.write(data_a)

swapFileData()