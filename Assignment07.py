# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# JEdwards,Dec 5, 2020,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# import pickle # This imports code from another code file!
# customer_id = int(input("Enter an Id: "))
# customer_name = str(input("Enter a Name: "))
# customer_list = [customer_id, customer_name]
# print(customer_list)
# # Now we store the data with the pickle.dump method
# objFile = open("AppData.dat", "ab")
# pickle.dump(customer_list, objFile)
# objFile.close()
# # And, we read the data back with the pickle.load method
# objFile = open("AppData.dat", "rb")
# objFileData = pickle.load(objFile) #load() only loads one row of data.
# objFile.close()
# print(objFileData)

try:
    quotient = 5 / 0
    print(quotient)
except:
    print("There was an error!")

try:
    f = open("test.txt")
except:
    print("There was an error!")



# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    pass  # TODO: Add code here

def read_data_from_file(file_name):
    pass  # TODO: Add code here

# Presentation ------------------------------------ #
# TODO: Get ID and NAME From user, then store it in a list object
# TODO: store the list object into a binary file
# TODO: Read the data from the file into a new list object and display the contents