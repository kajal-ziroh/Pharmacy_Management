from database import mycursor, mydb
from manager import Manager
from admin import Admin
from user_operation import can_view_medicines

# Welcome message
print("Welcome to the Pharmacy Management System!")

# Registration or Login
while True:
    user_choice = input("Enter '1' for registration or '2' for login: ")
    if user_choice == '1':
        # Registration
        name = input("Enter your name: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        is_admin = input("Are you an admin? Enter 'y' for Yes or 'n' for No: ")
        is_manager = input("Are you a pharmacy manager? Enter 'y' for Yes or 'n' for No: ")

        if is_admin == 'y':
            is_admin = 1
        else:
            is_admin = 0

        if is_manager == 'y':
            is_manager = 1
        else:
            is_manager = 0

        sql = "INSERT INTO users (name, username, password, is_admin, is_manager) VALUES (%s, %s, %s, %s, %s)"
        val = (name, username, password, is_admin, is_manager)
        mycursor.execute(sql, val)
        mydb.commit()

        print("Registration successful! Please login to continue.")

    elif user_choice == '2':
        # Login
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        val = (username, password)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        if result:
            user_id = result[0]
            is_admin = result[4]
            is_manager = result[5]

            if is_admin == 1:
                print("Welcome Admin!")
                while True:
                    admin_choice = input("Enter '1' to view all pharmacy managers or '2' to view all medicines: ")
                    admin = Admin()

                    if admin_choice == '1':
                        admin.view_all_managers()
                    elif admin_choice == '2':
                        admin.view_all_medicines()
                    else:
                        print("Invalid choice. Please try again.")
            elif is_manager == 1:
                print("Welcome Pharmacy Manager!")
                while True:
                    print("\nPlease select an option:")
                    print("1. Add medicine")
                    print("2. View medicine")
                    print("3. Delete medicine")
                    print("4. Exit")

                    choice = input("Enter your choice (1-4): ")
                    manager = Manager()
                    if choice == '1':
                        manager.add_medicine()

                    elif choice == '2':
                        manager.view_medicines()
                    elif choice == '3':
                        manager.delete_medicine()
                    elif choice == '4':
                        print("Thank you for using the Pharmacy Management System!")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Welcome User!")
                while True:
                    user_choice = input("Enter '1' to view medicines or '2' to exit: ")
                    if user_choice == '1':
                        can_view_medicines()
                    elif user_choice == '2':
                        break
                    else:
                        print("Invalid choice. Please try again.")
        else:
            print("Invalid username or password. Please try again.")

    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
