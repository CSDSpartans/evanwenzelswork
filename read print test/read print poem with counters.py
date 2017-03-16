name_of_mydocument = 'tuesdayafternoon.txt'
file_input = open(name_of_mydocument, 'r')     

line = file_input.readline()
line = file_input.readline()
line = file_input.readline()

line = file_input.readline()

line_counter = 0
stanza_counter = 1
total_lines_in_file = 3

while line != '':                      
    total_lines_in_file += 1
    if line == '\n':
      stanza_counter += 1
      print ()
    elif line_counter <= 8:
      line_counter += 1
      print(line_counter, ")   ", line, end = '')
    elif line_counter >= 9:
      line_counter += 1
      print(line_counter, ")  ", line, end = '')
    line = file_input.readline()
    
  



print ()
print ()
print ("The total number of stanzas in this poem are: ",  stanza_counter)
print ("The total number of lines in this file are: ", total_lines_in_file)
print ("Tuesday Afternoon first appeared in the alblum Days of Future Passed in 1967.")
print ("The members of The Moody Blues are Justin Hayward, John Lodge, and Graeme Edge.")

file_input.close()
