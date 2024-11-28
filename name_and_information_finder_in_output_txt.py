#read the output file 
#ask user for name input 
#search for it in the file 

output_file = "output.txt"

try: 
    #read the output file 
    with open(output_file, "r") as file:
        #this reads each lines in the file
        lines = file.readlines
    #ask user for name input
        name_search = input("Who are you searching for?: ")
except FileNotFoundError:
    print("File not found")
