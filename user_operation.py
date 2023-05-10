from database import mycursor


def can_view_medicines():
    # Select all medicines from the database
    sql = "SELECT * FROM medicines"
    mycursor.execute(sql)
    result = mycursor.fetchall()

    if result:
        print("Available Medicines:")
        print("SR.No   Medicine Name   Qty   Added Date   Added By   Price")
        print("----------------------------------------------------------------")
        for row in result:
            print(f"{row[0]}       {row[1]}       {row[2]}     {row[3]}       {row[4]}       {row[5]}")
    else:
        print("No medicines available.")
