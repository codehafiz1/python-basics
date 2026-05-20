import os
location = os.getcwd()
print(f"I'm working in {location}")
#for current Directory

files = os.listdir()
print(f"These are Files in my Folder {files}")
#for listing all files in current Folder

os.makedirs("folder_by_oslibrary",exist_ok=True)
print("New Folder is created")
#Creates a new Folder

exists = os.path.exists("First_Project.py")
print(f"Does a file named First_Project.py exists? {exists}")
#Check if a file is in the folder 

if exists:
    size = os.path.getsize("First_Project.py")
    print(f"file's Size : {size} Bytes")
#Get File Size