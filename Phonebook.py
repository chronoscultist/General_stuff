def add(name,number,dictionary,aliases):
    if name in dictionary:
        print("name already in list")
        return
    if name in aliases:
        print("name is already an alias")
        return
    dictionary[name] = number
    print("Name and number added")

def lookup(dictionary,name,aliases):
    if name in dictionary:
        print(dictionary[name])
    elif name in aliases:
        print(dictionary[aliases[name]])
    else:
        print ("name or alias not found")

def alias(dictionary,name,alias,aliases):
    for n, t in dictionary.items():
        if n == alias:
            print(n, t)
            print("cannot assign a")
            return
    if alias in aliases:
        print("alias is already assigned to a name")
        return
    if name in dictionary:
        aliases[alias]=name
        print("alias has been assigned to",name)
    elif name in aliases:
        aliases[alias]=aliases[name]
        print("alias has been assigned to",name)
    else:
        print("name not found")

def change(dictionary, name, number, aliases):

    for n,t in dictionary.items():
        if t == number:
            print(n,t)
            print("messed up")
            return

    if name in dictionary:
        dictionary[name] = number
        print("number has been changed for", name)

    elif name in aliases:
        dictionary[aliases[name]] = number
        print("Number has been changed via alias for", name)

    else:
        print("name not found, number has not been changed.")

def save(filename,dictionary,aliases):
    f = open(filename+".txt", "w")
    for n,t in dictionary.items():
        string = t + ";" + n + ";\n"
        f.write(string)
    for n,t in aliases.items():
        string = dictionary[t] + ";" + n + ";\n"
        f.write(string)
    f.close()
    print(filename,"has been saved")
def load(filename,dictionary, aliases):
    dictionary.clear()
    aliases.clear()
    filename=filename+".txt"
    try:
        with open(filename, "r") as a_file:
            while True:
                a=a_file.readline()
                if a=="":
                    return
                a = a.split(';')
                dictionary[a[1]]=a[0]
                print(filename,"has been accessed")
                print(dictionary)
    except FileNotFoundError:
        print("you got gotted, file dosent exist Boiiii")
def telefonbok():
    dictionary={}
    aliases={}
    print("Menu for phonebook")
    print("add name x: Add a name and number")
    print("alias name alias: Add a alias to a name and number")
    print("lookup name: Search for a name/alias and a number")
    print("save filename: Saves name and number into text file")
    print("load filename: Loads the content of a file")
    print("quit: Exit program:")
    while True:
        indata = input("telebok> ")
        I=indata.split()
        try:
            if I[0] == "add":
                add(I[1],I[2],dictionary,aliases)
                continue
            if I[0] == "lookup":
                lookup(dictionary,I[1],aliases)
                continue
            if I[0] == "alias":
                alias(dictionary,I[1],I[2],aliases)
                continue
            if I[0] == "change":
                change(dictionary, I[1],I[2], aliases)
                continue
            if I[0] == "save":
                save(I[1],dictionary, aliases)
                continue
            if I[0] == "load":
                load(I[1],dictionary,aliases)
                continue
            if I[0] == "quit":
                print("Exiting program...")
                return
        except IndexError:
            print('blev fel, get yo shit together son')

telefonbok()
