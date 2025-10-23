"""
File io: File I/O (Input/Output) means reading data from files and writing data to files using Python.
Manual steps:
1. Open notepad and create file
2. Write in the file
3. Close the file

Mode:
Read mode: r
write mode: w
Append mode: a
Read/write: r+
"""
# If you don't mention the exact path, then it will create a file in same location
# f = open("Writedemo.txt", "w")
# If you mention the exact path, then it will create a file in that location
path = "C:\\Users\\ashok\\PycharmProjects\\cloned_project\\my_python_selenium_pytest_git_jenkins_learnings\\TestingConcepts\\Files\\"
f = open(path + "Writedemo.txt", "r+")   # Change here "w/a/a+" and observe the changes in file
f.write("Hello, Welcome to the Python World\n")
lis = [65, 78, 989, 877, 8787]
for i in lis:
    f.write(str(i)+"\n")

f.close()

f = open(path + "Writedemo.txt", "r")
print(f.read())     # reads all the file and prints on console
# print(f.readline())     # Reads line by line
