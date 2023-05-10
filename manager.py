# from database import mydb, mycursor
#
#
# def register():
#     medicine_name = input("Enter the medicine name: ")
#     quantity = input("Enter the quantity: ")
#     added_date = input("Enter the date added (YYYY-MM-DD): ")
#     added_by = input("Enter the name of the person who added the medicine: ")
#     price = input("Enter the price: ")
#
#     sql = "INSERT INTO medicines (medicine_name,quantity, added_date, added_by, price) VALUES (%s, %s, %s, %s, %s)"
#     val = (medicine_name,quantity , added_date, added_by, price)
#     mycursor.execute(sql, val)
#     mydb.commit()
#
#     print("Medicine added successfully!")
#
#
# def view():
#     mycursor.execute("SELECT * FROM medicines")
#     rows = mycursor.fetchall()
#
#     if not rows:
#         print("No medicines found!")
#     else:
#         print("SR.No\tMedicine Name\tQty\tAdded Date\tAdded By\tPrice")
#         for i, row in enumerate(rows):
#             sr_no = i + 1
#             name = row[1]
#             qty = row[2]
#             added_date = row[3]
#             added_by = row[4]
#             price = row[5]
#             print(f"{sr_no}\t{name}\t{qty}\t{added_date}\t{added_by}\t{price}")
#
#
# def delete():
#     name = input("Enter the name of the medicine to be deleted: ")
#
#     sql = "DELETE FROM medicines WHERE name = %s"
#     val = (name,)
#     mycursor.execute(sql, val)
#     mydb.commit()
#
#     print("Medicine deleted successfully!")

from database import mydb, mycursor


class Manager:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def add_medicine(self):
        medicine_name = input("Enter the medicine name: ")
        quantity = input("Enter the quantity: ")
        added_date = input("Enter the date added (YYYY-MM-DD): ")
        added_by = self.name
        price = input("Enter the price: ")

        sql = "INSERT INTO medicines (medicine_name,quantity, added_date, added_by, price) VALUES (%s, %s, %s, %s, %s)"
        val = (medicine_name, quantity, added_date, added_by, price)
        mycursor.execute(sql, val)
        mydb.commit()

        print("Medicine added successfully!")

    def view_medicines(self):
        mycursor.execute("SELECT * FROM medicines")
        rows = mycursor.fetchall()

        if not rows:
            print("No medicines found!")
        else:
            print("SR.No\tMedicine Name\tQty\tAdded Date\tAdded By\tPrice")
            for i, row in enumerate(rows):
                sr_no = i + 1
                name = row[1]
                qty = row[2]
                added_date = row[3]
                added_by = row[4]
                price = row[5]
                print(f"{sr_no}\t{name}\t{qty}\t{added_date}\t{added_by}\t{price}")

    def delete_medicine(self):
        name = input("Enter the name of the medicine to be deleted: ")

        sql = "DELETE FROM medicines WHERE medicine_name = %s"
        val = (name,)
        mycursor.execute(sql, val)
        mydb.commit()

        print("Medicine deleted successfully!")
