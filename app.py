

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



 
 
    def register(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        id = len(users) + 1
        print(id)

        for user in users:
            current_person = users[user]
            if name == current_person.name:
                print("name exists")

        new_person = User(name,password,id)

        users[id] = new_person
        print(users[id])        
