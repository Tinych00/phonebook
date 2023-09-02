# Function to register a new user
def register_user():
    username = input("Enter a username: ")
    with open("phonebook.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if username in line:
                print("Username already exists. Try a different username.")
                return
    password = input("Enter a password: ")
    with open("phonebook.txt", "a") as file:
        file.write(f"{username}:{password}\n")
    print("User registered successfully!")


# Function to log in
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("phonebook.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                print("Login successful!")
                return
    print("Invalid username or password. Please try again.")


# Main program loop
while True:
    print("Phonebook Program")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        register_user()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    input("Press Enter to continue...")
    # This will clear the screen to create a fresh display after each interaction
    print("")
