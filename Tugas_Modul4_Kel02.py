list = ["A", "B", "C", "D", "E", "F"]
def showlist():
    print("Antrian saat ini: ", end='')
    for i in list:
        print(f"{i} <- ", end = '')
    print("\n")