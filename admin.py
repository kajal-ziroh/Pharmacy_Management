# from database import mycursor, mydb
#
#
# def view_all_managers():
#     sql = "SELECT * FROM users WHERE is_manager = 1"
#     mycursor.execute(sql)
#     result = mycursor.fetchall()
#
#     if result:
#         print("List of all pharmacy managers:")
#         for row in result:
#             print(f"ID: {row[0]}, Name: {row[1]}, Username: {row[2]}, Password: {row[3]}")
#     else:
#         print("No pharmacy managers found.")
#
#
# def view_all_medicines():
#     sql = "SELECT * FROM medicines"
#     mycursor.execute(sql)
#     result = mycursor.fetchall()
#
#     if result:
#         print("List of all medicines:")
#         for row in result:
#             print(
#                 f"ID: {row[0]}, Name: {row[1]}, Quantity: {row[2]}, Added Date: {row[3]}, Added By: {row[4]}, Price: {row[5]}")
#     else:
#         print("No medicines found.")

from database import mycursor, mydb


class Admin:
    def view_all_managers(self):
        sql = "SELECT * FROM users WHERE is_manager = 1"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        if result:
            print("List of all pharmacy managers:")
            for row in result:
                print(f"ID: {row[0]}, Name: {row[1]}, Username: {row[2]}, Password: {row[3]}")
        else:
            print("No pharmacy managers found.")

    def view_all_medicines(self):
        sql = "SELECT * FROM medicines"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        if result:
            print("List of all medicines:")
            for row in result:
                print(
                    f"ID: {row[0]}, Name: {row[1]}, Quantity: {row[2]}, Added Date: {row[3]}, Added By: {row[4]}, Price: {row[5]}")
        else:
            print("No medicines found.")
