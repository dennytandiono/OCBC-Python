numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 
  725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 
  219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 
  907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
  399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 
  626, 949]


def get_number_even(numbers):
    for number in numbers:
        if number % 2 == 0 :
            print(number, end=" ")
        else: 
            continue

        if number == 918: 
            break

    print("\n")
    print("Looping Done!")


def get_number_odd(numbers):
    for number in numbers:
        if number != 918: 
            if number % 2 == 1 :
                print(number, end=" ")
            else:
                continue
        else:
            print("\n")
            break
    print("Looping Done!")


def menu():
    print("SELAMAT DATANG DI MENU ODD EVEN")
    print("===============================")
    print("Silahkan Pilih Menu")
    print("[1] Bilangan Genap ( Requirement Awal , Titik Berhenti 918)")
    print("[2] Bilangan Ganjil ( Custom Requirement , Titik Berhenti 918")
    print("[0] Exit Program")

menu()
pilihan = int(input("Masukkan Pilihan [0-2]: "))

while pilihan !=0:
    if pilihan == 1:
        get_number_even(numbers)
        pass
    elif pilihan == 2:
        get_number_odd(numbers)
        pass
    else:
        print("invalid option")

    print()
    menu()
    pilihan = int(input("Masukkan Pilihan [0-2]: "))

print("Goodbye!")




