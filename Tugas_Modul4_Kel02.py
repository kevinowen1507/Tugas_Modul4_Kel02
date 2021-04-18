list = ["A", "B", "C", "D", "E", "F"]
def showlist():
    print("Antrian saat ini: ", end='')
    for i in list:
        print(f"{i} <- ", end = '')
    print("\n")
def addlist():
    a = str(input("Silahkan masukkan nama"))
    list.append(a)
    print(a, "telah ditambahkan ke dalam antrian")
def removelist():
    showlist()
    a = int(input("Pilih nomor urut yang ingin dihapus: "))
    del list[a-1]
def nextturn():
    print("\nGiliran selanjutnya:", list[0], "silahkan masuk\n")
    del list[0]
