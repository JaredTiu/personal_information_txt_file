def valid_name(name_search):
    for x in name_search: 
        if not x.isalpha() or x == "":
            return False
        elif all(x.isalpha() or x.isspace() for x in name_search):
            return True 

output_file = "output.txt"

try:   
    #read the output file 
    with open(output_file, "r") as file:
        #this reads each lines in the file
        read = file.readlines()
            #ask user for name input
        while True:
            name_search = input("Who are you searching for?(enter the full name): ").lower()
            while not valid_name(name_search) or name_search.isspace() or name_search.strip() == "":
                name_search = input("please enter a valid name: ")
            exists = False
        
            for i, line in enumerate(read): 
                if line.startswith("Name: ") and name_search in line.lower():
                    print("\nPerson Found. \n")
                    print("\nDisplaying Information: \n")
                
                    for n in range(i, i + 7):
                        if n <= len(read):
                            print(read[n], end= "")
                            
                    exists = True
                    break
        
            if exists == False:
                print(f"The is no person {name_search} found in the txt file.")
                print("REMINDER TO INPUT FIRST NAME, MIDDLE NAME, AND SURNAME")

            if_continue = input("Do you want to find another person the txt file?(y/n): ")

            if if_continue != "y":
                print("Exiting...")
                break

except FileNotFoundError:
    print("File not found")