import mysql.connector
import random
import base64
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QCheckBox
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setGeometry(200, 200, 900, 600)
        self.setWindowTitle('Manage Every Password | M.E.P')

        self.initUI()
    
    def initUI(self):
        self.b1 = QPushButton(self)
        self.b1.setText('Add New')
        self.b1.clicked.connect(genPassword)
        
        self.checkSpecial = QCheckBox(self)
        self.checkSpecial.setText('Special Character')
        self.checkSpecial.move(0, 25)

    def clicked(self):
        self.label.setText('You pressed the button.')

masterPassword = 'some_secret_key' #the secret key for the encryption and decryption. (encrypt to database. when loging in encrypt and match)
myPassword = 'password' #will be the list of passwords to decrypt from the data base or new one to encrypt to database
   
def connectDB():
    print("DataBase connection.")
    mydb = mysql.connector.connect(host='192.168.1.85', user='pi', password='69mNQ^7z*8')

    myCursor = mydb.cursor()

    myCursor.execute('SELECT * FROM passwordManager.test;')

    rows = []

    for row in myCursor:
        rows.append(row)
    
    print('Gathered all rows.')
    return rows

def getChracter(characterNumber):
    if characterNumber == 1:
        return 'a'
    elif characterNumber == 2:
        return 'A'
    elif characterNumber == 3:
        return 'b'
    elif characterNumber == 4:
        return 'B'
    elif characterNumber == 5:
        return 'c'
    elif characterNumber == 6:
        return 'C'
    elif characterNumber == 7:
        return 'd'
    elif characterNumber == 8:
        return 'D'
    elif characterNumber == 9:
        return 'e'
    elif characterNumber == 10:
        return 'E'
    elif characterNumber == 11:
        return 'f'
    elif characterNumber == 12:
        return 'F'
    elif characterNumber == 13:
        return 'g'
    elif characterNumber == 14:
        return 'G'
    elif characterNumber == 15:
        return 'h'
    elif characterNumber == 16:
        return 'H'
    elif characterNumber == 17:
        return 'i'
    elif characterNumber == 18:
        return 'I'
    elif characterNumber == 19:
        return 'j'
    elif characterNumber == 20:
        return 'J'
    elif characterNumber == 21:
        return 'k'
    elif characterNumber == 22:
        return 'K'
    elif characterNumber == 23:
        return 'l'
    elif characterNumber == 24:
        return 'L'
    elif characterNumber == 25:
        return 'm'
    elif characterNumber == 26:
        return 'M'
    elif characterNumber == 27:
        return 'n'
    elif characterNumber == 28:
        return 'N'
    elif characterNumber == 29:
        return 'o'
    elif characterNumber == 30:
        return 'O'
    elif characterNumber == 31:
        return 'p'
    elif characterNumber == 32:
        return 'P'
    elif characterNumber == 33:
        return 'q'
    elif characterNumber == 34:
        return 'Q'
    elif characterNumber == 35:
        return 'r'
    elif characterNumber == 36:
        return 'R'
    elif characterNumber == 37:
        return 's'
    elif characterNumber == 38:
        return 'S'
    elif characterNumber == 39:
        return 't'
    elif characterNumber == 40:
        return 'T'
    elif characterNumber == 41:
        return 'u'
    elif characterNumber == 42:
        return 'U'
    elif characterNumber == 43:
        return 'v'
    elif characterNumber == 44:
        return 'V'
    elif characterNumber == 45:
        return 'w'
    elif characterNumber == 46:
        return 'W'
    elif characterNumber == 47:
        return 'x'
    elif characterNumber == 48:
        return 'X'
    elif characterNumber == 49:
        return 'y'
    elif characterNumber == 50:
        return 'Y'
    elif characterNumber == 51:
        return 'z'
    elif characterNumber == 52:
        return 'Z'
    elif characterNumber == 53:
        return '1'
    elif characterNumber == 54:
        return '2'
    elif characterNumber == 55:
        return '3'
    elif characterNumber == 56:
        return '4'
    elif characterNumber == 57:
        return '5'
    elif characterNumber == 58:
        return '6'
    elif characterNumber == 59:
        return '7'
    elif characterNumber == 60:
        return '8'
    elif characterNumber == 61:
        return '9'
    elif characterNumber == 62:
        return '0'
    elif characterNumber == 63:
        return '!'
    elif characterNumber == 64:
        return '@'
    elif characterNumber == 65:
        return '#'
    elif characterNumber == 66:
        return '$'
    elif characterNumber == 67:
        return '%'
    elif characterNumber == 68:
        return '^'
    elif characterNumber == 69:
        return '&'
    elif characterNumber == 70:
        return '*'

def genPassword():
    print("Can generate new passwords.")
    # Generate 5 passwords and take the first one that either has a special character or not depending on check box

    number = 5

    passwordLength = random.randint(8, 12)
    generatedPasswords = []

    while len(generatedPasswords) < number:
        generatedPasswords.append("")

    if number > 0:
        print(str(number) + ' password(s) being generated. Please wait...')
        while number > 0:

            while len(generatedPasswords[number - 1]) < passwordLength:
                r = random.randint(1, 70)
                generatedPasswords[number - 1] += getChracter(r)

            print('Password #' + str(number) + ':')
            print(generatedPasswords[number - 1])
            number -= 1

def encryptPassword(key, string):
    print("Can encrypt passwords.")
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 128)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    arr2 = bytes(encoded_string, 'utf-8')
    return base64.urlsafe_b64encode(arr2)

def decryptPassword(key, string):
    print("Can decrypt passwords.")
    encoded_chars = []
    string = base64.urlsafe_b64decode(string)
    string = string.decode('utf-8')
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) - ord(key_c) % 128)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return encoded_string

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    
    win.show()
    sys.exit(app.exec_())

def loadGUI():
    print("Currently being worked on.")
    window()

loadGUI()

#print(connectDB())

#genPassword()

#encrypted = encryptPassword(masterPassword, myPassword)
#print('enc: {}'.format(encrypted))

#decrypted = decryptPassword(masterPassword, encrypted)
#print('dec: {}'.format(decrypted))
