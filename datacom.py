#ABA Module: Database Commands
#Author: Nathan Shah
#Date: Updated: April 15, 2021
#PLEASE READ: Before intial use need to create database via datacom.UserDatabase()

import pickle

class UserDatabase:
    """
    Models the user database.
    """
    def __init__(self):
        self.users = {}
        
        open("datacomFile.txt", "x")
        with open("datacomFile.txt", "wb") as f:
            pickle.dump(self.users, f)

        f.close()
        
class User:
    """
    A class that stores the information of the given user.
    """
    def __init__(self, username):
        self.username = username
        self.contacts = {}

class Record:
    """
    The record conatins the information about a particular record.
    """
    def __init__(self, recordID, SN = None, GN = None, PEM = None, WEM = None, PPH = None,
                WPH = None, SA = None, CITY = None, PC = None):
        self.recordID = recordID
        self.SN = SN
        self.GN = GN
        self.PEM = PEM
        self.WEM = WEM
        self.PPH = PPH
        self.WPH = WPH
        self.SA = SA
        self.CITY = CITY
        self.PC = PC

def addRecord(username, recordID, SN = None, GN = None, PEM = None, WEM = None, PPH = None,
                WPH = None, SA = None, CITY = None, PC = None):
    """
    Adds a record to the given users contacts.
    """
    if not check(recordID, SN, GN, PEM, WEM, PPH, WPH, SA, CITY, PC):
        return None
    else:
        users = openDatabase()

        users.values()

        if users.get(username, None) == None:
            users[username] = User(username)

        if len(users[username].contacts) == 256:
            print("Number of records exceeds maximum")
            return None
        
        if users[username].contacts.get(recordID, None) == None:
            users[username].contacts[recordID] = Record(recordID, SN, GN, PEM, WEM, PPH, WPH, SA, CITY, PC)
        else:
            print("Duplicate recordID")
            return None

        print("OK")
        saveDatabase(users)

def check(recordID, SN = None, GN = None, PEM = None, WEM = None, PPH = None,
                WPH = None, SA = None, CITY = None, PC = None):
    """
    Validates Inputs to addRecord method
    """

    if recordID == '':
        print("No recordID")
        return False
    
    if len(recordID) > 64:
        print("Invalid recordID")
        return False

    fieldValue = [SN, GN, PEM, WEM, PPH, WPH, SA, CITY, PC]

    for value in fieldValue:
        if value == None:
            continue
        if len(value) > 64:
            print("One or more invalid record data fields")
            return False

    return True
    
def deleteRecord(username, recordID):
    """
    Deletes a record from the given users contacts.
    """

    users = openDatabase()

    if recordID == '':
        print("No recordID")
        return None
    
    if len(recordID) > 64:
        print("Invalid recordID")
        return None

    if users[username].contacts.get(recordID, None) == None:
        print("RecordID not found")
        return None
    
    users[username].contacts.pop(recordID)

    print("OK")

    saveDatabase(users)

    return None
    
def editRecord(username, recordID, SN = None, GN = None, PEM = None, WEM = None, PPH = None,
                WPH = None, SA = None, CITY = None, PC = None):
    """
    Edits a record from the given users contacts.
    """

    if not check(recordID, SN, GN, PEM, WEM, PPH, WPH, SA, CITY, PC):
        return None
    else:
        users = openDatabase()

        if users[username].contacts.get(recordID, None) == None:
            print("RecordID not found")
            return None

        if SN != None:
            users[username].contacts[recordID].SN = SN
        if GN != None:
            users[username].contacts[recordID].GN = GN
        if PEM != None:
            users[username].contacts[recordID].PEM = PEM
        if WEM != None:
            users[username].contacts[recordID].WEM = WEM
        if PPH != None:
            users[username].contacts[recordID].PPH = PPH
        if WPH != None:
            users[username].contacts[recordID].WPH = WPH
        if SA != None:
            users[username].contacts[recordID].SA = SA
        if CITY != None:
            users[username].contacts[recordID].CITY = CITY
        if PC != None:
            users[username].contacts[recordID].PC = PC

        print("OK")
        
        saveDatabase(users)

    return None

def readRecord(username, recordID, SN = None, GN = None, PEM = None, WEM = None, PPH = None,
                WPH = None, SA = None, CITY = None, PC = None):
    """
    Prints the requested information to the user about th record of interest.
    """
    if recordID == '':
        print("No recordID")
        return None
    
    if len(recordID) > 64:
        print("Invalid recordID")
        return None

    fieldValues = [SN, GN, PEM, WEM, PPH, WPH, SA, CITY, PC]
    accecptedFieldValues = ['SN', 'GN', 'PEM', 'WEM', 'PPH', 'WPH', 'SA', 'CITY', 'PC', None]

    for value in fieldValues:
        if value not in accecptedFieldValues:
            print("Invalid fieldname(s)")
            return None
    
    users = openDatabase()

    if users[username].contacts.get(recordID, None) == None:
        print("RecordID not found")
        return None
                
    output = recordID

    total = 0
    for value in fieldValues:
        if value == None:
            total += 1
    
    if total == len(fieldValues):
        output = (output + ' SN=' + exist(users[username].contacts[recordID].SN) + ' GN=' + exist(users[username].contacts[recordID].GN)
                        + ' PEM=' + exist(users[username].contacts[recordID].PEM) + ' WEM=' + exist(users[username].contacts[recordID].WEM)
                        + ' PPH=' + exist(users[username].contacts[recordID].PPH) + ' WPH=' + exist(users[username].contacts[recordID].WPH)
                        + ' SA=' + exist(users[username].contacts[recordID].SA) + ' CITY=' + exist(users[username].contacts[recordID].CITY)
                        + ' PC=' + exist(users[username].contacts[recordID].PC) )

    else:
        for value in fieldValues:
            if value == None:
                continue   
            if value == 'SN':
                output = output + ' SN=' + users[username].contacts[recordID].SN
            if value == 'GN':
                output = output + ' GN=' + users[username].contacts[recordID].GN
            if value == 'PEM':
                output = output + ' PEM=' + users[username].contacts[recordID].PEM
            if value == 'WEM':
                output = output + ' WEM=' + users[username].contacts[recordID].WEM
            if value == 'PPH':
                output = output + ' PPH=' + users[username].contacts[recordID].PPH
            if value == 'WPH':
                output = output + ' WPH=' + users[username].contacts[recordID].WPH
            if value == 'SA':
                output = output + ' SA=' + users[username].contacts[recordID].SA
            if value == 'CITY':
                output = output + ' CITY=' + users[username].contacts[recordID].CITY
            if value == 'PC':
                output = output + ' PC=' + users[username].contacts[recordID].PC

    print(output)
    print("OK")

    return None

def exist(value):
    """
    Helpful function for readRecord
    """
    if value == None:
        return ''
    else:
        return value

def importDatabase(username, filename):
    """
    Imports the database of contacts in the form of a csv
    """

def exportDatabase(username, filename):
    """
    Exports a users database in the form of a csv
    """

def openDatabase():
    """
    Opens the databaseFile.txt
    """
    with open("datacomFile.txt", "rb") as f:
        users = pickle.load(f)
        f.close()
    
    return users

def saveDatabase(users):
    with open("datacomFile.txt", "wb") as f:
        pickle.dump(users,f)
    
    f.close()

    return None