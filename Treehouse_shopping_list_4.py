#create an empty list
shopping_list = []

#clear items from the list
def clear_all():
    del shopping_list[:]


#move items in the list
def move_item(old_idx, new_idx):
    index_old = old_idx - 1
    index_new = new_idx - 1
    item = shopping_list.insert(index_new, shopping_list.pop(index_old))
    print("Moved {} to new spot.".format(shopping_list[index_new]))
    show_list()


#remove items from the list
def remove_item(idx):
    index = idx - 1
    item = shopping_list.pop(index)
    print("Remove {}.".format(item))


#tell user what to do
def show_help():
    print("\nSeparate each item with a comma.")
    print("Type DONE to quit, SHOW to see the current list, REMOVE to delete an item and HELP to get this message.")


#display the list items
def show_list():
    count = 1
    for item in shopping_list:
        print("{}: {}".format(count, item))
        count += 1


#prompt the user to enter a list
print("Give me a list of things you want to shop for.")
show_help()

#start an infinite loop
while True:

    new_stuff = raw_input("> ")

    #do stuff based on what user asked
    if new_stuff == "DONE":
        print ("\nHere's your list:")
        show_list()
        break
    elif new_stuff == "HELP":
        show_help()
        continue
    elif new_stuff == "SHOW":
        show_list()
        continue
    elif new_stuff == "REMOVE":
        show_list()
        idx = input("Which item? Tell me the number: ")
        remove_item(int(idx))
        continue
    elif new_stuff == "CLEAR":
        clear_all()
        continue
    elif new_stuff == "MOVE":
        show_list()
        old_idx = input("Which item? Tell me the number: ")
        test = int(old_idx)
        print("You want to move " + shopping_list[test-1])
        new_idx = input("Where would you like to move it to? Tell me the number: ")
        move_item(int(old_idx), int(new_idx))
    else:
        #put the stuff into the list
        new_list = new_stuff.split(",")
        #allow insertion at end of list, or at a given spot
        index = raw_input("Add this at a certain spot? Press enter for the end of the list, "
            "or give me a number. Currently {} items in the list.".format(len(shopping_list)))
        if index:
            #check that a valid number was entered
            try:
                spot = int(index) - 1
            except ValueError:
                print("You didn't enter a number. Try again.")
                continue

            #if a valid number was entered, insert it but first get rid of extra stuff
            for item in new_list:
                shopping_list.insert(spot, item.strip())
                #increment the spot in case there's more than one list element
                spot += 1
        else:
            #if the user just hits enter, add the new items to the end of the list.
            for item in new_list:
                shopping_list.append(item.strip())
