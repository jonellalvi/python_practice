
# raw data:
phone_book = {
    "Jonell": {"name": "Jonell Alvi", "phone": "503-333-3333", "address": "3335 SE Taylor St. Portland OR"},
    "Jamil": {"name": "Jamil Alvi", "phone": "971-222-2222", "address": "9999 RockStar Ln. Portland OR"},
    "Ben":{"name": "Ben Alvi", "phone": "000-666-9999", "address": "1 Best Kid Ever St. Portland OR"}
    }

def Search():
    record_to_find = raw_input("Enter key to search:")
    print(phone_book[record_to_find])

def Add():
    name = raw_input("Enter name: ")
    number = raw_input("Enter phone number: ")
    address = raw_input("Enter addy: ")
    phone_book[name] = {"name": name, "number": number, "address": address}

    #phone_book[name] = raw_input("Enter data to add <<name, number, address>>: ")


def Delete():
    record_to_delete = raw_input("Enter key to Delete: ")

    if record_to_delete in phone_book:
        if raw_input("Are you sure? (y/n)") == "y":
            phone_book.pop(record_to_delete)
            print("Record Deleted")
    else:
        print("Record not found")
        print("Here's the list of Records:")
        print(phone_book.keys())




# ask what they want to do:
# while makes the if statement loop until you type Quit (break)
while True:
    test = str.lower(raw_input("What would you like to do? Type Search, Add, Delete, or Quit: "))

    if test == "Search":
        Search()
    elif test == "Add":
        Add()
    elif test == "Delete":
        Delete()
    elif test == "Quit":
        break
    else:
        print("Oops. Typo. Try again")
        #continue


