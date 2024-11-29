#read the output file 
#ask user for name input 
#search for it in the file 

output_file = "output.txt"

try: 
    #read the output file 
    with open(output_file, "r") as file:
        #this reads each lines in the file
        read = file.readlines()
    #ask user for name input
        name_search = input("Who are you searching for?: ")
        # exists = False
        # information = []

        for i, line in enumerate(read): 
            if line.startswith("Name: ") and name_search in line: 
            # if name_search in line:
                print(read[i], end= "")
                print(read[i + 1], end= "")
                print(read[i + 2], end= "")
                print(read[i + 3], end= "")
                print(read[i + 4], end= "")
                print(read[i + 5], end= "")
                # print(read[i + 6], end= "")


                # exists = True
                # information = line[i:i+6] #since every person has six lines between them
                # break

except FileNotFoundError:
    print("File not found")

# print(information)