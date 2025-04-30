#Ask the user what acronym they want to add to the file
#Then ask the user for the definition of the acronym  
#Open the file in append mode and write the acronym and definition to the file
#Write the new acronym and definition to the file
#Ask the user if they want to add another acronym
#If the user wants to add another acronym, repeat the process
#If the user does not want to add another acronym, print a message saying that the acronyms have been added to the file
#Close the file

acronym = input("What acronym would you like to add?\n")
definition = input("What is the definition of the acronym?\n")

with open('acronyms.txt', 'a') as file:
    file.write(acronym + "-" + definition + "\n")
   