#read the output file 
#ask user for name input 
#search for it in the file 

output_file = "output.txt"

information = []
try: 
    #read the output file 
    with open(output_file, "r") as file:
        #this reads each lines in the file
        
    #ask user for name input
        name_search = input("Who are you searching for?: ")
        exists = False

        for i in file: 
            if i.startswith("Name:") and name_search in file: 
                exists = True
                information = file[i:i+6] #since every person has six lines between them
                break

except FileNotFoundError:
    print("File not found")

print(information)