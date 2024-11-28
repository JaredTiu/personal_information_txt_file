file_txt = open("./output.txt", "w")

#get the personal info and store in a array 
#make a loop asking if the user wants to continue 
#write the stored value in the array in the txt file

name_array = []
age_array = []
date_of_birth_array = []
magic_sarap_array = []
converted_array = []

while True: 

    name = input("Input name: ")
    name_array.append(name)

    age = int(input("Input age: "))
    age_array.append(age)

    date_of_birth = input("Input your date of birth: ")
    date_of_birth_array.append(date_of_birth)

    magic_sarap = input("Binibilang mo ba ang butil ng magic sarap? y/n: ")
    magic_sarap_array.append(magic_sarap)
    
    for i in magic_sarap_array:
        if i == "y":
            converted_array.append("Yes")
        elif i == "n":
            converted_array.append("No")
        else: 
            print("Invalid input")
            input("Input again, binibilang mo ba ang butil ng magic sarap? y/n: ")
    
    for i in name_array:
        file_txt.write(f"Name: {i} \n" )
    for i in age_array:
        file_txt.write(f"Age: {i} \n" )
    for i in date_of_birth_array:
        file_txt.write(f"Date of birth: {i} \n" )
    for i in converted_array: 
        file_txt.write(f"Binibilang mo ba ang magic sarap?: {i} \n\n" )

    retry = input("Do you want to contiue? y/n: ")

    if retry != "y": 
        break