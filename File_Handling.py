
import requests
import os
class file:
    name='abc'
    user=0

    def getName(self):
        print("Welcome!")
        self.name = input("Enter your name: ")
        print("Hello",self.name )        
        self.getInput()

    def getInput(self):
        self.user = input("What do you want?\nClick 1 for Read File or Click 2 for Append or Create if doesn't exist or Click 3 for Write in Existing File or Create if it doesn't Exist or Click 4 for Create File or Click 5 for Clear A File or Enter Text in it: ")
        self.begin()

    def begin(self):
        if self.user == '1':
            self.readfile()
        elif self.user == '2':
            self.append()
        elif self.user == '3':
            self.write()
        elif self.user == '4':
            self.createfile()
        elif self.user == '5':
            self.clearfile()
        else: 
            print('Invalid Input')
            self.startOver()

    def end(self):
        print("You are out")

    def readfile(self):
        f = open("hello.txt", "r")
        print(f.read())
        f.close()
        self.startOver()


    def append(self):
        f = open("hello.txt", "a")
        print(f.write(" Everything will be fine!"))
        f.close()
        f = open("hello.txt","r")
        print(f.read())
        self.startOver()

    def write(self):
        f = open("hello.txt", "w")
        print(f.write("Everything will be OK!"))
        f.close()
        f = open("hello.txt","r")
        print(f.read())
        self.startOver()

    def createfile(self):
        f = open("hello.txt", "x") 
        # f = open("myfile.txt","w")
        self.startOver()

    def clearfile(self):
        if os.path.exists("file.txt"):
            os.remove("file.txt")
        else:
            print("The file does not exist")
        self.startOver()
        
    def startOver(self):
        inp = input("Press 0 to start Over or Press 1 to continue: ")
        if inp == '0':
            self.getName()
        elif inp == '1':
            self.getInput()
        else:
            print("Invalid Input")
            self.end()

        # f = open("hello.txt", "rt")
        # print(f.read())
        # f.close()

obj = file()
obj.getName()