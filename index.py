print("\nWelcome in bank system\n")
print("Login to panel")
print("(Password: password)")

password = input("\nType password: ")
name = input("Your name: ")

if password == "password":
    print("\nWelcome " + name)
else:
    print("\nAccess denied")

input("\nPress Enter to exit\n")