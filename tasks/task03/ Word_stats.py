import re
print("Welcome to Word Statistic Tool!")
menu = "1"
while menu == "1":
    print("Please type the text. Complete your text entry by double-tapping Enter key:")
    liststr = []
    while True:
        inp = input()
        if inp != "":
            inp = re.split(r'[:; ,*.!?\n]+',inp.lower())
            if inp[-1] == "":
                inp.pop()
            liststr.append(inp)
        else:
            break
    print("word\t\tcount\tfirst line\n___________________________________________")
    i = 0 
    for istr in liststr:
        j = 0
        for iword in istr:
            if iword == "":
                j += 1
                continue
            count = 1
            for a in range(i, len(liststr)):
                if (a == i) and (j < len(liststr[a])-1):
                    startb = j+1
                else:
                    startb = 0
                for b in range(startb, len(liststr[a])):
                    if liststr[a][b] == iword:
                        count += 1
                        liststr[a][b] = ""
            j += 1
            print(f"{iword}\t\t{count}\t{i}")
        i += 1
    menu=input("If you want to restart the program, enter 1. Press any other key to exit:")