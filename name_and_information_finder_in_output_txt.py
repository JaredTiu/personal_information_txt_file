#read the output file 
#ask user for name input 
#search for it in the file 

output_file = "output.txt"

information = []
try: 
    #read the output file 
    with open(output_file, "r") as file:
        #this reads each lines in the file
        lines = file.readlines
    #ask user for name input
        name_search = input("Who are you searching for?: ")

    for i in lines: 
        if lines.strip().startswith("Name: ") and name_search in lines: 
            exists = True
            information = lines[i:i+6] #since every person has six lines between them
            break

except FileNotFoundError:
    print("File not found")

print(information)