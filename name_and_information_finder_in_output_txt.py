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
        name_search = input("Who are you searching for?(enter the full name): ")
        exists = False

        for i, line in enumerate(read): 
            if line.startswith("Name: ") and name_search in line.lower():
                for n in range(i, i + 7):
                    if n <= len(read):
                        print(read[n], end= "")
                        break
        exists = True

        if exists == False:
            print(f"The is no person {name_search} found in the txt file.")
    

except FileNotFoundError:
    print("File not found")

# print(information)