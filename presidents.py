import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Presidents                          |
# Tiegan Cozzie                                        |
# Last Modified: November 2, 2021       |
# ---------------------------------------
# This program will give information about the presidents and past occupations
# The user can chose what information they want from options 1-6
# ---------------------------------------

class President:
    def __init__(self, first, last, number, start_in, term, occupations):
        self.number=number
        self.start_in=start_in
        self.term=term
        self.occupations=occupations
        self.name=first+" "+last
        self.first=first
        self.last=last

    def get_name(self):
        return self.name
    def get_number(self):
        return self.number
    def get_occupation(self):
        return self.occupations
    def get_average_term_length(self):
        return self.term

    def __str__(self):
        ans= "No. "+str(self.number)+"  ("+str(self.start_in)+")  "+self.name
        return ans

# Finds if the name inputed by the user is a president or not
# If the inputed name is a president it will offer all the information about that president
def print_by_name(pres_listing, name):
    result=False
    # Asks the user for more clerification if they put  in 3 or less characters
    if len(name)<3:
        print("\nPlease write full name")
    else:
        for presidents in pres_listing:
            # If name inputed matches with a president, their information will be printed
            if name==presidents.first.lower() or name==presidents.last.lower():
                print(presidents)
                result=True
    # If no president is found with the name given
    if result==False:
        print("No president's name contains "+"'"+name+"'")

# When a user askes what president was at a specific number, the respective president will be printed
def print_by_number(pres_listing, number):
    for presidents in pres_listing:
        # Checks to see if number inputed matches number of any president
        if number==int(presidents.number):
            print(presidents)

# The user inputs a specific occupation and will output how many presidents had said occupation and which ones
def count_by_occupation(pres_listing,occupation):
    # Keeps track of how many presidents have inputed occupation
    count=0
    # Keeps track of each presidents name
    picked=[]
    for presidents in pres_listing:
        for job in presidents.occupations:
            # Compares job inputed with presidents previous jobs and appends them to list "picked"
            if occupation==job:
                picked.append(presidents.name)
    if len(picked)==0:
        print(str(count)+" "+ occupation+" presidents")
    else:
        # Creating an empty string that selected presidents could be added to
        final=""
        # This is a new filtered listed for the picked list which checks for presidents being repeated more then once
        half_final=[]
        for x in picked:
            # Checks if a president has been repeated more then once
            if x not in half_final:
                half_final.append(x)
        for x in half_final:
            count+=1
            # Conjugates presidents into a string
            final= final+" "+str(x)+","
        print(str(count)+" "+occupation+" presidents: " + final)

# Takes average term length of every president
def average_term_length(pres_listing):
    ave=0
    pres=0
    for presidents in pres_listing:
        pres+=1
        ave+=presidents.term
    ave=ave/pres
    ave=round(ave,2)
    print("Average term length, about",ave,"years")
    


# ---------------------------------------

def print_menu():
    print ("""
1. Print all presidents
2. Print president by name
3. Print president by number
4. Count presidents with occupation
5. Print average term length
6. Quit
    """)
# ---------------------------------------

def print_all_presidents(pres_listing):
    for president in pres_listing:
        print(president)
    
# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pres_listing(filename):
    pres_listing = []
    file = open(filename, "r")
    
    for president in file:
        presilist = president.strip().split(",")
        number = int(presilist[0])               # number
        last = presilist[1]                      # last name
        first = presilist[2]                     # first name
        start_in = int(presilist[3])             # first year in office
        term = float(presilist[4])               # years in office
        occupations = []
        for position in range(5, len(presilist)):
            occupations += [presilist[position]] # occupation
        pres_listing += [President(first, last, number, start_in, term, occupations)]

    file.close()
    return pres_listing

# ---------------------------------------

def get_choice(low, high, message):
    
    legal_choice = False
    answer = input(message)
    while answer == "":
        answer = input(message)
    for char in answer:
        if char not in string.digits:
            print('ERROR: ', answer, "is not a number")
            return 0
    answer = int(answer)
    if (low > answer) or (answer > high):
        print('ERROR: ', answer, "is not a choice")
        print('\nPresident number must be between 1 and 46')
        return 0

    return answer

# ---------------------------------------

def main():
    pres_listing = create_pres_listing("pres_listing.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            print_all_presidents(pres_listing)
        elif choice == 2:
            name = input("Enter a president name: ").lower()
            print_by_name(pres_listing, name)
        elif choice == 3:
            number = get_choice(1, 46, "Enter a president number: ")
            print_by_number(pres_listing, number)
        elif choice == 4:
            occupation = input("Enter a president occupation: ").lower()
            count_by_occupation(pres_listing, occupation)
        elif choice == 5:
            average_term_length(pres_listing)
        elif choice == 6:
            print("Thank you.  Goodbye!")

# ---------------------------------------

main()
