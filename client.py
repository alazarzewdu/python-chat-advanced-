def menu():
    print("1. Send Text")
    print("2. Send File")
    print("3. Video Stream")
    # print("4. Exit")


menu()
option = int(input("Enter your option:"))

while option != 0:
    if option == 1:
        print("1 is called")
        break
    elif option == 2:
        print("2 is called")
        break
    elif option == 3:
        print("3 is called")
        break
    else:
        print("Invalid Option")

print()
menu()
option = int(input("Enter your option:"))


print("Thanks for using this program")