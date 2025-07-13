file = open("new_file_assignment.txt", "r")     #open the file in read mode
#read the contents of the file and then print it. 
contents = file.read()  
print(contents)
file.close()  #closing the file is good habit
