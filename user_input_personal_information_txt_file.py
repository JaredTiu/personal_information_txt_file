import datetime
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

    date_of_birth = (input("Input your date of birth: "))
    # converted_date = datetime.datetime.strptime(f"%B %d, %Y", {date_of_birth} ).strftime("%m/%d/%y")
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

    retry = input("Do you want to contiue? y/n: ")

    if retry != "y": 
        break

for i in range(len(name_array)):
    file_txt.write(f"Name: {name_array[i]} \n" )
    file_txt.write(f"Age: {age_array[i]} \n" )
    file_txt.write(f"Date of birth: {date_of_birth_array[i]} \n" )
    file_txt.write(f"Binibilang mo ba ang magic sarap?: {converted_array[i]} \n\n" )