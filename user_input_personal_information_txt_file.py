file_txt = open("./output.txt", "w")

#get the personal info and store in a array 
#make a loop asking if the user wants to continue 
#write the stored value in the array in the txt file

name_list = []
while True: 

    name = input("Input name: ")
    name_list.append(name)

    retry = input("Do you want to contiue? y/n: ")

    if retry != "y": 
        break

file_txt.write(name_list)