#read the output file 
#ask user for name input 
#search for it in the file 

output_file = "output.txt"


with open(output_file, "r") as file:
   print(file.read())
