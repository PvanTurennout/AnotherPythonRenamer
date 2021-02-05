import os

def printException(exception):
    print(exception.args[0])


def getBulkInfo():
    try:
        newName = getNewName()
    except Exception as e:
        printException(e)
    bulkRename(newName)


def getRenameInfo():
    try:
        currentName = getCurrentName()
        newName = getNewName()
    except Exception as e:
        printException(e)
    renameFile(currentName, newName)


def getCurrentName():
    name = input("enter current file name:  ")
    try:
        return str(name)
    except ValueError:
        raise Exception("That's not a valid name")


def getNewName():
    name = input("enter new file name:  ")
    try:
        return str(name)
    except ValueError:
        raise Exception("That's not a valid name")


def currentDirectory():
    # return os.path.dirname(os.path.realpath(__file__)) + "\\filder\\"
    return os.getcwd()


def renameFile(oldName: str, newName: str):
    try:
        os.rename(currentDirectory() + oldName, currentDirectory() + newName)
    except FileNotFoundError:
        print("This file does not exist")


def getFilesInDir():
    list_of_files = []

    for root, dirs, files in os.walk(currentDirectory()):
        for file in files:
            list_of_files.append(file)
    
    return list_of_files


def checkFileTypes(files):
    controlFile = files[0]
    fileType = controlFile.split(".")[1]

    for thing in files:
        if thing.split(".")[1] != fileType:
            raise Exception("Files must be of same type")
    
    return "." + fileType


def bulkRename(name):
    files = getFilesInDir()
    i = 1

    try:
        fileType = checkFileTypes(files)
    except Exception as e:
        printException(e)
    
    for file in files:
        renameFile(file, name + str(i) + fileType)
        i += 1


def listAllFilesInDir():
    files = getFilesInDir()
    for file in files:
        print(file)
    
    input("Press a enter to continue...")

