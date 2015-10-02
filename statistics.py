#project2015-P0010.py
#A statistics gathering program with a menu.

# import modules needed
import time

# Define global variables



# comment out the timezone list as appropriate
# This list is the conversion of GMT to PacificDST (-7)
pacific = ["17","18","19","20","21","22","23","0 ","1 ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","11","12","13","14","15","16"]
# This list is the conversion of GMT to PacificSTD (-8)
#pacific = ["16","17","18","19","20","21","22","23","0 ","1 ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","11","12","13","14","15"]

# The list below is for reference only
# GMT      ["0 ","1 "," 2","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]


#Then we setup the functions

def savestat(): #define a function 
    # This function is to gather the current date and time
    # and build the data string to write to the statistics file

    # Open the statistics file for writing as "output"
    output = open("c:\data\stats.txt", "a")

    # Get the current date (information as listed
    h = time.strftime("%H", time.gmtime()) # get Hour
    M = time.strftime("%M", time.gmtime()) # get Minute
    m = time.strftime("%m", time.gmtime()) # get month
    d = time.strftime("%d", time.gmtime()) # get day of month
    Y = time.strftime("%Y", time.gmtime()) # get Year
    j = time.strftime("%j", time.gmtime()) # get julian day
    H = pacific[int(h)] # Adjust for timezone by converting h to an integer and putting the value from list pacific(h) in H, the hour variable
    
    # Prep the statistics line
    export= str("{},{},{},{},{},{},{},\n").format(roption,j,Y,m,d,H,M) # Build the entry for the statistics file
    print export # For debugging
    output.write(export)# Write one line to statistics file

    # Be nice and close the file to keep file up to date and avoid data loss
    output.close() 


# Below is the menu selection

ans = True #Prime ans for the while, menu entry, loop

while ans :
    # The menu display
          print """
       What Service did you render?
                       Reference type
       1X- Informational - Brief (Hours, policy, looking up single item in catalog)
       2X- Informational - Extended (Searching stacks, ILL help, holds, reserves, finding classrooms)
       3X- Reference (Multistep search for materials/resources)
       4X- Point of Service Instruction (How to search catalog/databases, citing sources, editing, formatting)

                       Interaction type
       X1- In person
       X2- By Phone
       X3- Chat (Real Time)
       X4- Email(Asynchronus)
        9- Quit

	   
	   Please enter two digits, first the reference type then the interaction type and press enter. 
	   ex. 14 for Information by email.
                """
          roption = "11"   # Declare and preload roption
          
          roption = raw_input("Please make a selection ",)    # Input a choice, prefaced with a message, and place in roption

          try:                          # setup to handle enter without entry
                option = int(roption)   # make sure menu entry is number
                if option == 11:        #test for 11, if not 11 continue down test tree
                        savestat()      #Call the defined function savestat
                elif option == 12:      # This seems like the simplest way to test the input for valid entrys
                        savestat()      # and go on to the savestat function, writing the choice to the file
                elif option == 13:
                        savestat()
                elif option == 14:
                        savestat()
                elif option == 21:
                        savestat()
                elif option == 22:
                        savestat()
                elif option == 23:
                        savestat()
                elif option == 24:
                        savestat()
                elif option == 31:
                        savestat()
                elif option == 32:
                        savestat()
                elif option == 33:
                        savestat()
                elif option == 34:
                        savestat()
                elif option == 41:
                        savestat()
                elif option == 42:
                        savestat()
                elif option == 43:
                        savestat()
                elif option == 44:
                        savestat()
                elif option ==  9:     #test for nine, end program cleanly
                        ans = False    # That's all folks!
                elif option == 99:     #test for nine, end program cleanly
                        ans = False    # That's all folks!
                else:                  # what to do if entry not a tested value
                        print "oops, try again!" 
          except ValueError:           # how to deal with no entry or wrong type of entry
                        print "oops, try again!!"

print """
Find your data file at c:\data\statistics.txt
The record format is statistic,julian date,year,month,day,hour(24),minute
      """
        
