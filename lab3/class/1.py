class StringManipulator:
    def getString(self):
        self.user_input = input("Enter a string: ")

    def printString(self):
        print(self.user_input.upper())


str_manip = StringManipulator()
str_manip.getString()  
str_manip.printString()  