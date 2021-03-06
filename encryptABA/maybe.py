#ABA Module: Database Commands
#Author: Nathan Shah
#Date: Updated: April 15, 2021
#PLEASE READ: Before intial use need to create database via datacom.UserDatabase()

import pickle
import csv
from cryptography.fernet import Fernet #noqa

class UserDatabase:
    """
    Models the user database.
    """
    def __init__(self):
        self.users = {}
        
        try:
            self.key = Fernet(Fernet.generate_key())
            self.saveDatabase(self.users)

        except FileExistsError:
            return None
            

    def openDatabase(self):
        """
        Opens the databaseFile.txt
        """
        # opening the encrypted file
        with open('datacomFile.txt', 'rb') as enc_file:
            encrypted = enc_file.read()
  
        # decrypting the file
        decrypted = self.key.decrypt(encrypted)
  
        # opening the file in write mode and
        # writing the decrypted data
        with open('datacomFile.txt', 'wb') as dec_file:
            dec_file.write(decrypted)

        with open("datacomFile.txt", "rb") as f:
            users = pickle.load(f)
            f.close()
        
        return users

    def saveDatabase(self,users):
        with open("datacomFile.txt", "wb") as f:
            pickle.dump(users,f)
        
        f.close()

        with open('datacomFile.txt', 'rb') as file:
            original = file.read()
        
        # encrypting the file
        encrypted = self.key.encrypt(original)
    
        # opening the file in write mode and 
        # writing the encrypted data
        with open('datacomFile.txt', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        return None
class User:
    """
    A class that stores the information of the given user.
    """
    def __init__(self, username):
        self.username = username.strip()
        self.contacts = {}

class Record:
    """
    The record conatins the information about a particular record.
    """
    def __init__(self, recordID, SN = None, GN = None, PEM = None, WEM = None, PPH = None,
                WPH = None, SA = None, CITY = None, STP = None, CTY = None, PC = None):
        self.recordID = recordID
        if SN == None: 
            self.SN = '' 
        else: 
            self.SN = SN
        if GN == None:
            self.GN = ''
        else:
            self.GN = GN
        if PEM == None:
            self.PEM = ''
        else:
            self.PEM = PEM
        if WEM == None:
            self.WEM = ''
        else:
            self.WEM = WEM
        if PPH == None:
            self.PPH = ''
        else:
            self.PPH = PPH
        if WPH == None:
            self.WPH = ''
        else:
            self.WPH = WPH
        if SA == None:
            self.SA = ''
        else:
            self.SA = SA
        if CITY == None:
            self.CITY = ''
        else:
            self.CITY = CITY
        if STP == None:
            self.STP = ''
        else:
            self.STP = STP
        if CTY == None:
            self.CTY = ''
        else:
            self.CTY = CTY
        if PC == None:
            self.PC = ''
        else:
            self.PC = PC

def addRecord(UserDatabase,username, recordID, SN = None, GN = None, PEM = None, WEM = None, PPH = None,
                WPH = None, SA = None, CITY = None, STP = None, CTY= None, PC = None,):
    """
    Adds a record to the given users contacts.
    """
    if not check(recordID, SN, GN, PEM, WEM, PPH, WPH, SA, CITY, STP, CTY, PC):
        return None
    else:
        users = UserDatabase.openDatabase()

        if username not in users:
            users[username] = User(username)

        if len(users[username].contacts) == 256:
            print("Number of records exceeds maximum")
            return None
        
        if recordID not in users[username].contacts:
            users[username].contacts[recordID] = Record(recordID, SN, GN, PEM, WEM, PPH, WPH, SA, CITY, STP, CTY, PC)
        else:
            print("Duplicate recordID")
            return None

        print("OK")
        UserDatabase.saveDatabase(users)

def check(recordID, SN = None, GN = None, PEM = None, WEM = None, PPH = None,
                WPH = None, SA = None, CITY = None, STP = None, CTY= None, PC = None):
    """
    Validates Inputs to addRecord method
    """

    if recordID == '':
        print("No recordID")
        return False
    
    if len(recordID) > 64:
        print("Invalid recordID")
        return False

    fieldValue = [SN, GN, PEM, WEM, PPH, WPH, SA, CITY, STP, CTY, PC]

    for value in fieldValue:
        if value == None:
            continue
        if len(value) > 64:
            print("One or more invalid record data fields")
            return False

    return True
    
def deleteRecord(UserDatabase,username, recordID):
    """
    Deletes a record from the given users contacts.
    """

    users = UserDatabase.openDatabase()

    if username not in users:
        users[username] = User(username)

    if recordID == '':
        print("No recordID")
        return None
    
    if len(recordID) > 64:
        print("Invalid recordID")
        return None

    if recordID not in users[username].contacts:
        print("RecordID not found")
        return None
    
    users[username].contacts.pop(recordID)

    print("OK")

    UserDatabase.saveDatabase(users)

    return None
    
def editRecord(UserDatabase,username, recordID, SN = None, GN = None, PEM = None, WEM = None, PPH = None,
                WPH = None, SA = None, CITY = None, STP = None, CTY= None, PC = None):
    """
    Edits a record from the given users contacts.
    """

    if not check(recordID, SN, GN, PEM, WEM, PPH, WPH, SA, CITY, STP, CTY, PC):
        return None
    else:
        users = UserDatabase.openDatabase()

        if recordID not in users[username].contacts:
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
        if STP != None:
            users[username].contacts[recordID].STP = STP
        if CTY != None:
            users[username].contacts[recordID].CTY = CTY
        if PC != None:
            users[username].contacts[recordID].PC = PC

        print("OK")
        
        UserDatabase.saveDatabase(users)

    return None

def readRecord(UserDatabase,username, recordID, SN = None, GN = None, PEM = None, WEM = None, PPH = None,
                WPH = None, SA = None, CITY = None, STP = None, CTY= None, PC = None):
    """
    Prints the requested information to the user about th record of interest.
    """
    if recordID == '':
        print("No recordID")
        return None
    
    if len(recordID) > 64:
        print("Invalid recordID")
        return None

    fieldValues = [SN, GN, PEM, WEM, PPH, WPH, SA, CITY, STP, CTY, PC]
    accecptedFieldValues = ['SN', 'GN', 'PEM', 'WEM', 'PPH', 'WPH', 'SA', 'CITY', 'STP', 'CTY', 'PC', None]

    for value in fieldValues:
        if value not in accecptedFieldValues:
            print("Invalid fieldname(s)")
            return None
    
    users = UserDatabase.openDatabase()
    UserDatabase.saveDatabase(users)

    if recordID not in users[username].contacts:
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
                        + ' STP=' + exist(users[username].contacts[recordID].STP)+ ' CTY=' + exist(users[username].contacts[recordID].CTY)
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
            if value == 'STP':
                output = output + ' STP=' + users[username].contacts[recordID].STP
            if value == 'CTY':
                output = output + ' CTY=' + users[username].contacts[recordID].CTY
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

def importDatabase(UserDatabase,username, filename):
    """
    Imports the database of contacts in the form of a csv
    """

    if filename == '':
        print("No Input_file specified")
        return None
    
    try:
        f = open(filename, 'r')
    except OSError:
        print("Can't open Input_file")
        return None

    if '.csv' not in filename:
        print("Input_file invalid format")
        return None

    with f:

        users = UserDatabase.openDatabase()
        

        if users.get(username, None) == None:
            users[username] = User(username)

        reader = csv.reader(f)

        totalLines = 0
        for row in reader:

            if row[0] in users[username].contacts:
                print("Duplicate recordID")
                users.pop(username)
                return None

            if totalLines == 256:
                print("Number of records exceeds maximum")
                users.pop(username)
                return None
            
            newRecord = Record(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                            row[7], row[8], row[9], row[10], row[11])

            users[username].contacts[row[0]] = newRecord


        UserDatabase.saveDatabase(users)

    return None

def exportDatabase(UserDatabase,username, filename):
    """
    Exports a users database in the form of a csv
    """
    users = UserDatabase.openDatabase()
    UserDatabase.saveDatabase(users)

    if filename == '':
        print("No Output_file specified")
        return None
    
    try:
        f = open(filename, 'w')
    except OSError:
        print("Can't open Output_file")
        return None

    strings = []
    for contact in users[username].contacts:
        output = ''
        output = (output + users[username].contacts[contact].recordID + ',' + users[username].contacts[contact].SN + ',' 
                    + users[username].contacts[contact].GN + ',' + users[username].contacts[contact].PEM + ',' 
                    + users[username].contacts[contact].WEM + ',' + users[username].contacts[contact].PPH + ',' 
                    + users[username].contacts[contact].WPH + ',' + users[username].contacts[contact].SA + ',' 
                    + users[username].contacts[contact].CITY + ',' + users[username].contacts[contact].STP + ','
                    + users[username].contacts[contact].CTY + ',' + users[username].contacts[contact].PC) + '\n'
        strings.append(output)

    try:
        f.writelines(strings)
    except:
        print("Error writing Output_file")
        return None
    
    print("OK")
    return None