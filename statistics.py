#project2015-P0010.py
#A statistics gathering program with a menu.

# import modules needed
import time

# Define global variables
# Open the statistics file for writing as "output"
output = open("c:\data\stats.txt", "a") 
pacific = ["5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","0","1","2","3","4"] 



#Then we setup the functions
def statrm11(): #define a function 
    # This function is for Informational, brief - in person
    # Get the current date (information as listed
    h = time.strftime("%H", time.gmtime()) # get Hour
    M = time.strftime("%M", time.gmtime()) # get Minute
    m = time.strftime("%m", time.gmtime()) # get month
    d = time.strftime("%d", time.gmtime()) # get day of month
    Y = time.strftime("%Y", time.gmtime()) # get Year
    j = time.strftime("%j", time.gmtime()) # get julian day
    H = pacific[int(h)] # adjust for timezone
    # Prep the statistics line
    export= str("{},{},{},{},{},{},{},\n").format(roption,j,Y,m,d,H,M)
    print export # For debugging
    output.write(export)# Write one line to statistics file

def statrm12(): #define a function 
    # This function is for Informational, brief - on phone
    # Get the current date (information as listed
    h = time.strftime("%H", time.gmtime()) # get Hour
    M = time.strftime("%M", time.gmtime()) # get Minute
    m = time.strftime("%m", time.gmtime()) # get month
    d = time.strftime("%d", time.gmtime()) # get day of month
    Y = time.strftime("%Y", time.gmtime()) # get Year
    j = time.strftime("%j", time.gmtime()) # get julian day
    H = pacific[int(h)] # adjust for timezone

    # Prep the statistics line
    export= str("{},{},{},{},{},{},{},\n").format(roption,j,Y,m,d,H,M)
    print export # For debugging

    output.write(export)# Write one line to statistics file
    
def statrm13(): #define a function with the variable to pass on inside ()
    # This function is for Informational, brief - by chat
    # Get the current date (information as listed
    h = time.strftime("%H", time.gmtime()) # get Hour
    M = time.strftime("%M", time.gmtime()) # get Minute
    m = time.strftime("%m", time.gmtime()) # get month
    d = time.strftime("%d", time.gmtime()) # get day of month
    Y = time.strftime("%Y", time.gmtime()) # get Year
    j = time.strftime("%j", time.gmtime()) # get julian day
    H = pacific[int(h)] # adjust for timezone
     
    # Prep the statistics line
    export= str("{},{},{},{},{},{},{},\n").format(roption,j,Y,m,d,H,M)
    print export # For debugging

    output.write(export)# Write one line to statistics file
    
    
def statrm14(): #define a function with the variable to pass on inside ()

    # This function is for Informational, brief - by email
    # Get the current date (information as listed
    h = time.strftime("%H", time.gmtime()) # get Hour
    M = time.strftime("%M", time.gmtime()) # get Minute
    m = time.strftime("%m", time.gmtime()) # get month
    d = time.strftime("%d", time.gmtime()) # get day of month
    Y = time.strftime("%Y", time.gmtime()) # get Year
    j = time.strftime("%j", time.gmtime()) # get julian day
    H = pacific[int(h)] # adjust for timezone

    # Prep the statistics line
    export= str("{},{},{},{},{},{},{},\n").format(roption,j,Y,m,d,H,M)
    print export # For debugging

    output.write(export)# Write one line to statistics file
    
def statrm21(): #define a function with the variable to pass on inside ()

    # This function is for Informational, extended - in person
    # Get the current date (information as listed
    h = time.strftime("%H", time.gmtime()) # get Hour
    M = time.strftime("%M", time.gmtime()) # get Minute
    m = time.strftime("%m", time.gmtime()) # get month
    d = time.strftime("%d", time.gmtime()) # get day of month
    Y = time.strftime("%Y", time.gmtime()) # get Year
    j = time.strftime("%j", time.gmtime()) # get julian day
    H = pacific[int(h)] # adjust for timezone

    # Prep the statistics line
    export= str("{},{},{},{},{},{},{},\n").format(roption,j,Y,m,d,H,M)
    print export # For debugging

    output.write(export)# Write one line to statistics file
    
def statrm22(): #define a function with the variable to pass on inside ()


     # This function is for Informational, extended - on phone
    # Get the current date (information as listed
    h = time.strftime("%H", time.gmtime()) # get Hour
    M = time.strftime("%M", time.gmtime()) # get Minute
    m = time.strftime("%m", time.gmtime()) # get month
    d = time.strftime("%d", time.gmtime()) # get day of month
    Y = time.strftime("%Y", time.gmtime()) # get Year
    j = time.strftime("%j", time.gmtime()) # get julian day
    H = pacific[int(h)] # adjust for timezone

    # Prep the statistics line
    export= str("{},{},{},{},{},{},{},\n").format(roption,j,Y,m,d,H,M)
    print export # For debugging

    output.write(export)# Write one line to statistics file
    
def statrm23(): #define a function with the variable to pass on inside ()


    # This function is for Informational, extended - by chat
    # Get the current date (information as listed
    h = time.strftime("%H", time.gmtime()) # get Hour
    M = time.strftime("%M", time.gmtime()) # get Minute
    m = time.strftime("%m", time.gmtime()) # get month
    d = time.strftime("%d", time.gmtime()) # get day of month
    Y = time.strftime("%Y", time.gmtime()) # get Year
    j = time.strftime("%j", time.gmtime()) # get julian day
    H = pacific[int(h)] # adjust for timezone

    # Prep the statistics line
    export= str("{},{},{},{},{},{},{},\n").format(roption,j,Y,m,d,H,M)
    print export # For debugging

    output.write(export)# Write one line to statistics file
    
def statrm24(): #define a function with the variable to pass on inside ()

    # This function is for Informational, extended - by email
    # Get the current date (information as listed
    h = time.strftime("%H", time.gmtime()) # get Hour
    M = time.strftime("%M", time.gmtime()) # get Minute
    m = time.strftime("%m", time.gmtime()) # get month
    d = time.strftime("%d", time.gmtime()) # get day of month
    Y = time.strftime("%Y", time.gmtime()) # get Year
    j = time.strftime("%j", time.gmtime()) # get julian day
    H = pacific[int(h)] # adjust for timezone

    # Prep the statistics line
    export= str("{},{},{},{},{},{},{},\n").format(roption,j,Y,m,d,H,M)
    print export # For debugging

    output.write(export)# Write one line to statistics file
    

# Below is the menu selection 
ans = True #Prime ans for the while, menu entry, loop
while ans :
          print """
       What Service did you render?
       
       1X- Informational - Brief (Hours, policy, looking up single item in catalog)
       2X- Informational - Extended (Searching stacks, ILL help, holds, reserves, finding classrooms)
       3X- Reference (Multistep search for materials/resources)
       4X- Point of Service Instruction (How to search catalog/databases, citing sources, editing, formatting)
       X1- In person
       X2- By Phone
       X3- Chat (Real Time)
       X4- Email(Asynchronus)
        9- Quit

	   
	   Please enter two digits, first the reference type then the interaction type. 
	   ex. 14 for Information by email.
                """
          roption = "11" # Preload roption
          roption = raw_input("Please make a selection ",)    # make a choice
          try:                          # setup to handle enter without entry
                option = int(roption) # make sure menu entry is number
                if option == 11:       #test for one
                        statrm11()   #Call the defined function statrmXX
                elif option == 12:
                        statrm12()
                elif option == 13:
                        statrm13()
                elif option == 14:
                        statrm14()
                elif option == 21:
                        statrm21()
                elif option == 22:
                        statrm22()
                elif option == 23:
                        statrm23()
                elif option == 24:
                        statrm24()		
                elif option ==  9:     #test for nine
                        print "Find your data file at c:\data\statistics.txt"
                        ans = False # That's all folks!
                else:                 # what to do if not tested
                        print "oops, try again!" 
          except ValueError:            # how to deal with no entry at all
                        print "oops, try again!!"

output.close() # be nice and close the file
        
