# Using readline()
file0 = open('C:/Users/RHolton1/Documents/Test Data for Python/multi_data1.csv', 'r')
# Opens file in read mode, must use forward slashes for file path
count = 0

while True:
    count += 1
# iterates through each line in file

    # Get next line from file
    line = file0.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break
    print("Line{}: {}".format(count, line.strip()))
    # will print the line count and string(s) according to the format parameters
    # in this case line.strip() means all non whitespace characters

print(count - 1)
# it's count minus 1 because I can't seem to just return the last number
#and otherwise it'll be 1 more than the count I want :/

file0.close()
#close the file we read from to prevent errors

file1 = 'C:/Users/RHolton1/Documents/Test Data for Python/multi_data1.csv'
with open(file1, "r") as f:
    #opening the first file in 'read' mode, renaming the variable to prevent trouble
    lines = f.readlines()
    #this function reads the line values, as a string, into a set
    print(lines)
    #spits out the strings for review, if I needed it
with open(file1, "w") as f:
    #sets the file to 'write' mode for working
    for line in lines:
        #so this says for a line now that exists in the 'lines' set we established above
        if line.strip("\n") != ",":
            #this will remove the character at the end that says "time for a new line!"
            f.write(line)
            #if it isn't just a comma (the separator in a csv), it will write the line

print("Empty lines removed!")
#just to know we got here with no errors

# Using readline()
#Same as the first part, just to review and confirm the data was updated!
file2 = open('C:/Users/RHolton1/Documents/Test Data for Python/multi_data1.csv', 'r')
count = 0

while True:
    count += 1

    # Get next line from file
    line = file2.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break
    print("Line{}: {}".format(count, line.strip()))

print(count - 1)

file2.close()

# with open("yourfile.txt", "r") as file_input:
#     with open("newfile.txt", "w") as output: 
#         for line in file_input:
#             if line.strip("\n") != "nickname_to_delete":
#                 output.write(line)