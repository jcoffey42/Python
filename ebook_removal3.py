# Created on a win system with IDLE

# Read in the deleted_ebooks file and make an array(list) of the titles
# Read in ebook.txt one line at a time and compare it to the Remove array
# Write that record2 line out to export.
# The goal is to extract the item id of ebooks the library will delete
# due to consortium ebook deletion.


print " first the houskeeping" # So you know we have started
# Open file for read only access, change the filename to your needs
record = open("c:\data\ebookRemoval\deleted_ebooks.txt", "r")

# Open a file for output, write access, change the filename to your needs
output = open("c:\data\ebookRemoval\export.txt","w")

# Open a file for output, write append access, change the filename to your needs
output3 = open("c:\data\ebookRemoval\etitle.txt","a")
output2 = open("c:\data\ebookRemoval\isbn.txt","a")

# Setup the empty lists
a = 0  # left of book id number in url
a1 = "&AN=" # Text to compare 
b = 0  # right of book id number in url
b1 = "&site="  # Text to compare 

w = "" # holds the element of WorkingRemove for testing
m = ""  # holds the result of finding the unique ID in the URL
m1 = "" # used as temp storage in the searching process
m2 = "" # used as temp storage in the searching process
n = ""  # temp storage for Remove[x] comparing the unique ID in url

u = "856  4"  ## Text to compare  for 856 field for URL
ui = 0   # element index in list of 856

isbn1 = "035 " # 035 field text to compare 
isbni = ""  # Temporary storage of isbn field. As 035 it holds any kind of system comtrol number
isbn = "" # The isbn snipped from isbn1
i = 0     # The element index of the isbn field

xxx = "not present" # put in list index 0 for to use missing fields. 

ExportTitle = "" # Temporary storage of Title and "|"
Title = []  # The Title of the removed ebook ooutput to the title.txt file to help locate failed comparisons

Remove = [] # The list of unique ID's snipped from the deleted list url's
r = "" # temporary storage of the unique ID while building WorkingRemove


WorkingRemove = [] # The entire input from, record, one file read, split by "|"

WorkingEbook = [] # The entire input from, record2, one file read, split by "|"

# Setup loop to read through entire file for processing
# Loads a line of text from the object record into lineuntil the file end
print " build the list of items being removed to search for" # So you know we started this 
for Line in record:
	
# Split the record into a list called WorkingRemove by the pipe symbol
      WorkingRemove = Line.split("|")

      m1 = WorkingRemove[4]   
      for x in range(0,(len(m1)-1)): # find the unique id location in this url
                   if m1[x:x+4] == a1: # find just before
                        a = x
                   
      for x in range(0,(len(m1)-1)): # find just after
                   if m1[x:x+6] == b1:
                        b = x
                   
      r =m1[a+4:b] # snip out the unique ID with the location found
     
      Remove.append(r) # Append the URL to the list WorkingRemove
      Title.append(WorkingRemove[0]) # Capture the title in matching index of Remove
      lengthRemove = len(Remove) # Change lengthRemove to the current length of the list WorkingRemove 
      




record.close() # Close the PDA list file

print "Now we search through the list of items comparing the uique book id to the one in our database and saving the isbn of that title."
# Open file for read only access, change the filename to your needs
record2 = open("c:\data\ebookRemoval\ebooksall2.txt", "r")

# The loop below will cycle throught eash record in the file of items from the library until it reaches the end.

for Line2 in record2:
      
      # Split the record into a list called WorkingCounter by the pipe symbol
      WorkingEbook = Line2.split("|")
      WorkingEbook.insert(0,xxx) # gives us a message for missing fields
      ui = 0 #Preload the "Not Present" message incase, good housekeeping
      i = 0  #Preload the "Not Present" message incase, good housekeeping

      for y in range(0,(len(WorkingEbook)-1)):
              
              w = WorkingEbook[y] # Put the field being tested in w

              if ui == 0:
                if w[:5] == u[:5]: # Test for the 856 field
                    ui=y           # This is the list index with the url and unique id in it
              if i == 0:                  
                if w[:4] == isbn1: # Test for the 035 field, that has the ISBN or other control number in it
                    i = y          # This is the list index with the control number in it

                  
    
      isbni = WorkingEbook[i] # Put the list item into isbn1 for editing
                         
      isbn = isbni[17:31] # Snip out the ISBN from surrounding data
       
      m2 = WorkingEbook[ui] # Copy the entire url to  m2
      m1 = m2[39:]  # Remove the local section by starting the copy after it

      for x in range(0,len(m1)):  # Find the unique id location in this url
              if m1[x:x+4] == a1: # Find just before the text just before
                   a = x          # The position just before the unique id
                   
      for x in range(0,len(m1)):   # Find the unique id location in this url
              if m1[x:x+6] == b1:  # Find the text just after the unique id
                   b = x           # The position just after the unique id
                   
      
      
      m =m1[a+4:b] # Snip out the unique ID with the locations just found and place it in m
      
      
      for x in range(0,len(Remove)): # Start the compaqrison loop based on the length of the Remove list
            
             n = Remove[x]      # Copy the deleted ID for testing to n         
             if  m == n: # Compare the current record ID to deleted ID first  

                 output.write(Line2)    # If it matches write out the entire record for reference
                 isbnout = isbni+"|"    # I choose to write out the entire 035 element due to variations in how the field was filled
                                        # Only half the items had an ISBN in the record
                                        # Simpler to use edit tools later to remove unwanted text 
                 ExportTitle = Title[x]+"|" # Build title with "|" delimeter  
                 output2.write(isbnout) # Append the isbnout field , the entire 035 field, to the file at output2
                 output3.write(ExportTitle) # Output the matched Title
                 
         
#Close the files and end
print " All Done!"
print lengthRemove # This is how many titles we tested for removal
print Remove       # This is the unique id snipped from the url for testing against
# Close all the files 
output.close()
output2.close()
output3.close()
record2.close()

raw_input() # To keep the window open on gui systems
