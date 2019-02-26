

class Menu():
    def display_menu(self):
        command = ""
        while command != "q":
            command = input("Enter 'r' to register 'l' to login and 'q' to quit: ")
            if command == "r":
                print("register")
            elif command == "l":
                print("login")
            elif command == "q":
                print("programm quited")



 
 
            