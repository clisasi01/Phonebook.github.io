# Python Programing By Chris Lisasi

entryList = []
while True:
    print '************* \nDevOps Phone Book \n1 - New Entry \n2 - Update Entry \n3 - Delete Entry \n4 - View'
    choice = raw_input('Please make a selection: ')
    validChoice = False
    while validChoice == False:
        if choice == '1' or choice == '2' or choice == '3' or choice == '4':
            validChoice = True
        else:
            choice = raw_input('Sorry "'"%s"'" is not a valid choice, please try again: '%(choice))
    if choice == '1':
        name = raw_input('Enter Name: ')
        num = raw_input('Enter Number: ')
        entry = '%s : %s'%(name,num)
        entryList.append(entry)
    if choice == '2':
        updateName = raw_input('Enter Name you would like to update: ')
        x = 0
        for names in entryList:
            if updateName in names:
                validUpdateChoice = False
                while validUpdateChoice == False:
                    confirm = raw_input('Do you want to update %s ? (Y/N): '%names)
                    if confirm.upper() == 'Y':
                        newName = raw_input('Enter New Name: ')
                        newNumber = raw_input('Enter New Number: ')
                        newEntry = '%s : %s'%(newName,newNumber)
                        entryList[x] = newEntry
                        validUpdateChoice = True
                    elif confirm.upper() == 'N':
                        validUpdateChoice = True
                    else:
                        print 'Choice not valid, try again'
            x = x + 1
    if choice == '3':
        deleteName = raw_input('Enter Name you would like to delete: ')
        x = 0
        for names in entryList:
            if deleteName in names:
                validUpdateChoice = False
                while validUpdateChoice == False:
                    confirm = raw_input('Do you want to delete %s ? (Y/N): '%names)
                    if confirm.upper() == 'Y':
                        entryList.remove(names)
                        validUpdateChoice = True
                    elif confirm.upper() == 'N':
                        validUpdateChoice = True
                    else:
                        print 'Choice not valid, try again'
            x = x + 1
        
    if choice == '4':
        for line in entryList:
            print line
