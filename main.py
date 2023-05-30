from query import Connect_DB
conn = Connect_DB()
# select_data = conn.select(1)
# print(select_data)

# insert_data = conn.insert('MICHAEL ANGELO RILAN', 23)
# print(insert_data)

# change_data = conn.change(1,'JOHN DOE',24)
# print(change_data)

# delete_data  = conn.remove(1)
# print(delete_data)


while True:
    choose = input("""Choose number you want to execute:\n\n
    1.) Select Data in database \n
    2.) Insert Data in the database \n
    3.) Edit Data from the database \n
    4.) Delete data from the datbase \n
    Press any key to stop the program...
    >>>
    """)

    if choose == '1':
        select_data = conn.select()
        print(select_data)

    elif choose == '2':
        name_in = input("Enter fullname: ")
        age_in = int(input("Enter your age: "))
        insert_data = conn.insert(name_in,age_in)
        print(insert_data)

    elif choose == '3':
        id_in = int(input("Enter id you wish to change : "))
        name_in = input("Enter full name: ")
        age_in = int(input("Enter age: "))
        change_data = conn.change(id_in,name_in,age_in)
        print(change_data)

    elif choose == '4':
        id_in = int(input("Enter id you wish to delete : "))
        delete_data = conn.remove(id_in)
        print(delete_data)

    else:
        print('Program ended')
        conn.closing_tags()
        break
    