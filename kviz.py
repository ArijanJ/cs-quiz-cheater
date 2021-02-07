from os import path, listdir, remove
import time
import sympy

search = 'Koliko je:  '

def log(string):
    logString = '[' + time.strftime('%H:%M:%S', time.localtime()) + ']: ' + str(string)
    print(logString)

def dirFile(path):
    return listdir(path)[0]

def findCondump():
    condumpNum = 0
    cstrikeFiles = listdir()

    for file in cstrikeFiles:
        if "condump" in file and '.txt' in file:
            condumpNum = file
            condumpNum = condumpNum.replace('condump', '').replace('.txt', '')

    with open(("condump" + str(condumpNum) + ".txt"), "r", encoding="ISO-8859-1") as condump:
        log("Last condump: " + condumpNum)
        lines = reversed(condump.readlines())


        with open('kvizExec.cfg', "a", encoding='ISO-8859-1') as execFile:
            execFile.truncate(0)

            for line in lines:

                line = line.rstrip()
                if search in line:
                    log("Found question: " + line)

                    result = calculateString(line.replace(search, ''))
                    log("Solution: " + str(result))

                    execFile.write('alias resiKviz \"say ' + str(result) + ' je odgovor na vase pitanje!\"')

                    condump.close()

                    remove("condump" + str(condumpNum) + ".txt")

                    return

def calculateString(str):
    try:
        return int(sympy.simplify(str))
    except:
        return

while(True):
    if len(listdir('kviz')) != 0:
        findCondump()
        remove(path.join("kviz", dirFile("kviz")))