class ExcelReader:
    @staticmethod
    def readExcelFile():
        print("Reading from Excel")


class MYSQLDBConnection:
    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL")

class TC1:
    def runTC(self):
        ExcelReader.readExcelFile() # Reading from Excel
        MYSQLDBConnection.readMySQLFile() # Reading from MySQL
        print("Hi from TC1") # Hi from TC1

class TC2:

    def runTC(self):
        ExcelReader.readExcelFile() # Reading from Excel
        MYSQLDBConnection.readMySQLFile() # Reading from MySQL
        print("Hi from TC2") # Hi from TC2

tc1 = TC1()
tc2 = TC2()
tc1.runTC()
tc2.runTC()