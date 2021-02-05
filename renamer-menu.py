from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem, MenuItem
from renamer import getBulkInfo, getRenameInfo, listAllFilesInDir, currentDirectory

def makeMenu():
    return ConsoleMenu("Renaming Tool")


def renameFunction():
    return FunctionItem("Rename File", getRenameInfo, [])


def bulkFunction():
    return FunctionItem("Bulk Rename", getBulkInfo, [])


def fileListFunction():
    return FunctionItem("List all Files in folder", listAllFilesInDir, [])

def space():
    print(currentDirectory())
    input("SPACE")


def test():
    return FunctionItem("current working directory", space, [])

def addFunctions(menu):
    menu.append_item(renameFunction())
    menu.append_item(bulkFunction())
    menu.append_item(fileListFunction())
    menu.append_item(test())


def menuInit():
    menu = makeMenu()
    addFunctions(menu)
    return menu


def main():
    menuInit().show()


if __name__ == "__main__":
    main()
