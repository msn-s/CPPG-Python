# ------------------------------------------
# Title: ICE5 - Student Presentations (Arrays and Lists)
# Author: Mason Hilder
# Date: July 8th 2025
# Purpose: To demonstrate your knowledge of arrays and lists in Python.
# ------------------------------------------

#region Declarations
studentList = []
ALLOW_DUPLICATES = False
is_running = True
is_Valid = True
menuText = """
------------------------------------
Main Menu
1. Add Student to the Queue
2. View Entire Student Queue
3. Call Next Student in Queue
4. Remove Student From Queue
5. Quit"""
#endregion

#region Main Application
print('-'*40)
print("Welcome to Mason's Student Queue Application!")
print('-'*40)
while is_running:
    print(menuText)
    
    try:
        choice = input("Enter your choice (e.g 1,2,3,4,5): ").strip() 
        choice = int(choice)
        if (choice >= 1 and choice <=5):
            is_Valid = True
            # Try and except statement to validate user input is in valid range (integer and between 1-5)
        else:
            is_Valid = False
            print("\nMust be in range 1-5")
    except ValueError:
        print("\nInput must be an integer")
        is_Valid = False
        # Exception handling , as well as leaving is_Valid flag false, reprompting the user to input a valid answer
    
    while is_Valid:
        # While the users input is validated; loop
        if choice == 1:
            studentName = input("\nEnter students name: ").strip()
            studentList.append(studentName)
            print("\n%s has been added to the queue" % (studentName))
            is_Valid = False
            # If choice = 2, take and store the users input, append it into the StudentList array
            # Resetting flag to exit the loop and reprompt user for another input

        elif choice == 2:
            print('-'*40)
            placement = 1
            for student in studentList:
                print("\n%s. %s" % (placement , student))
                placement += 1
                # Fancy looking print statement just to properly space the display of student names
            is_Valid = False
            # If choice = 2, iterate through every elememnt in studentList array and print
        elif choice == 3:
            print("The next person in queue is %s" %  (studentList[0]))
            is_Present = input("Is %s present today? (y/n): " % (studentList[0])).strip()
            if (is_Present == "y" or is_Present == "yes"):
                print("\n%s successfully removed from queue" % (studentList[0]))
                studentList.pop(0)
                # Doing math second as if i pop and then call [0] it will be different thne what i want it to be
                # If student is present, remove them from the list

            elif (is_Present == "n" or is_Present == "no"):
                absent_Student = studentList.pop(0)
                studentList.append(absent_Student)
                print("added %s to end of the queue" % (absent_Student))
                # If student is not present, put them at the back of the list
                
            else:
                print('\nAnswer must be "y" or "n"')
            is_Valid = False

        elif choice == 4:
            student = input("Enter the students name you want to remove (case sensitive): ").strip()
            if student in studentList:
                studentList.remove(student)
                # Storing input for student name to be removed
                print("\n%s removed from queue" % (student))
            else:
                print("\n%s is not in the list" % (student))
                # Data validation check to make sure that there is in fact a student present in list
            is_Valid = False 
        
        elif choice == 5:
            input("\nPress enter to exit the program...")
            is_running = False  
            is_Valid = False
            # Exitting main loop and inner loop
    if len(studentList) == 0:
        print("\nNo more students left in queue, you are done for the day!")
        input("Press enter to exit program...")
        is_running = False 
    # Setting flag to false to exit main loop and close program   







#endregion
