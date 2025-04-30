def find_acronym():
    look_up =input("What siftware acronym would you like to look up?\n")

    found = False
    with open('acronyms.txt') as file:
        for line in file:
            if look_up in line:
                print(line)
                found = True
                break
    if not found:
        print("Sorry, that acronym was not found.")

def add_acronym():
    acronym = input("What acronym would you like to add?\n")
    definition = input("What is the definition of the acronym?\n")
    with open('acronyms.txt', 'a') as file:
        file.write(acronym + "-" + definition + "\n")
        print("Great, the acronym has been successfully added to the file!")

def main(): 
#Ask the user if they want to add an acronym or look one up
    choice = input("Would you like to add an acronym or look one up? (add/look up)\n")
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()

main()