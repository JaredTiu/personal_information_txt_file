from datetime import datetime

def valid_name(name):
    for x in name: 
        if not x.isalpha() or x == "":
            return False
    return True 

def email_checker(email):
    character = ("@")

    if any((c in character) for c in email):
        return True 
    else: 
        return False

file_txt = open("./output.txt", "w")

name_array = []
age_array = []
date_of_birth_array = []
address_array = []
email_array = []
magic_sarap_array = []
converted_array = []

#get the personal info and store in a array 
while True: 
    name = input("Input name: ")
    while not valid_name(name) or name.isspace() or name.strip() == "":
       name = input("please enter a valid name: ")
    name_array.append(name)

    while True:    
        try: 
            age = int(input("Input age: "))

            if age <=0 or age >=120:
                raise
            age_array.append(age)
            break
        except:
            print("Enter a valid age. ")

    while True: 
        try:
            date_of_birth = (input("Input your date of birth (MM/DD/YY, Example: August 17, 2006): "))
            extracting_DoB = datetime.strptime(date_of_birth, "%B %d, %Y")
            converted_DoB = extracting_DoB.strftime("%m/%d/%y")
            date_of_birth_array.append(converted_DoB)
            break
        except:
            print("Please enter in MM/DD/YY format")

    address = input("Input your address here: ")
    address_array.append(address)

    email = input("Input your email here: ")
    while not email_checker(email):
        email = input("Please Input a valid email: ")
    email_array.append(email)

    magic_sarap = input("Binibilang mo ba ang butil ng magic sarap? y/n: ")
    magic_sarap_array.append(magic_sarap)
    
    for i in magic_sarap_array:
        if i == "y":
            converted_array.append("Yes")
        elif i != "y":
            converted_array.append("No")
        else: 
            print("Invalid input")
            input("Input again, binibilang mo ba ang butil ng magic sarap? y/n: ")
    
    #make a loop asking if the user wants to continue 
    retry = input("Do you want to contiue? y/n: ")

    if retry != "y": 
        print("Information has been printed in the txt file, Thank you.")
        break

#write the stored value in the array in the txt file
for i in range(len(name_array)):
    file_txt.write(f"Name: {name_array[i]} \n" )
    file_txt.write(f"Age: {age_array[i]} \n" )
    file_txt.write(f"Date of birth: {date_of_birth_array[i]} \n" )
    file_txt.write(f"Adress: {address_array[i]} \n" )
    file_txt.write(f"Email: {email_array[i]} \n" )
    file_txt.write(f"Binibilang mo ba ang magic sarap?: {converted_array[i]} \n\n" )