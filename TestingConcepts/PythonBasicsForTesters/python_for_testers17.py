"""
WITH Keyword: The advantage is that the file is properly closed
      after its suite finishes, even if an exception is raised at some point.
AS Keyword
"""

path = "C:\\Users\\ashok\\PycharmProjects\\cloned_project\\my_python_selenium_pytest_git_jenkins_learnings\\TestingConcepts\\Files\\"
with open(path+"demofile.txt", "w") as fw:
    fw.write("This file is created using WITH and AS keywords")

with open(path+"demofile.txt", "r") as fr:
    print(fr.read())