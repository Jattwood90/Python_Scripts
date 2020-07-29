import pandas as pd

def openCommand():
    print("Copy and paste the path to the txt file you wish to use: ", end="")
    return str(input())

def openTextFile(pathfile):
    with open(pathfile, 'r') as textfile:
        reader = textfile.readlines()
        out = []
        for items in list(reader):
            out.append(items.strip())
        return out

def reportCase(name):
    name = name.title()
    name = name.split()
    last = name[-1]
    last = last.upper()
    name.pop(-1)
    name.append(last)
    return ' '.join(name)


def runStuff(out):
    titleCaseList = []
    for elements in out:
        titleCaseList.append(reportCase(elements))
    return titleCaseList


if __name__ == "__main__":
    while True:
        try:
            fileInput = openCommand()
            files = openTextFile(fileInput)
            df = pd.DataFrame(runStuff(files)).to_csv('names.csv', index=None)
            print("Script finished. Check the folder/directory where this script is saved for 'name.csv' file.")
        except:
            Exception: FileNotFoundError
            print('The file path you entered is wrong, or does not exist')
        finally:
            print('Do you wish to try again? (Note name.csv will be overwritten if script is run again)\n'
                  'Press "Y" to rerun script. Press any other key to exit')
            userInput = str(input())
            if userInput == 'Y' or 'y':
                continue
            else:
                break
