#read the output file 
#ask user for name input 
#search for it in the file 

output_file = "output.txt"

try: 
    #read the output file 
    with open(output_file, "r") as file:
        #this reads each lines in the file
        read = file.readlines
    #ask user for name input
        name_search = input("Who are you searching for?: ")
        exists = False
        information = []

        for i in file: 
            # if i.startswith(name_search) in file: 
            if name_search in i: 
                exists = True
                information = file[i:i+6] #since every person has six lines between them
                break

except FileNotFoundError:
    print("File not found")

print(information)