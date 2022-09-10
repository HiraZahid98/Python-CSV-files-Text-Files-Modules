# w overwrites the file contents 
# open a witl with "with" keyword closes file automatically
# variable "file_to_work_with" is a handler 
# keyword  "open" open up the file if it exist otherwise it creates  a new file 
with open("index.txt", "w") as file_to_work_with:
    file_to_work_with.write("Have a nice day")

# open a file in order to read its content  use "r" 
# store  a file content in a variable 
with open("index.txt","r") as f:
    retrieve_content = f.read()
    print(retrieve_content)

# append a content in a file using "a"
with open ("index.txt","a") as f:
    f.write("\n It's a fresh morning today  ")