import sys

def helpText():
    print "'El nombre' is Spanish for 'THE Nombre'!"
    print "Usage: elnombre.py <Name list> <domain> <name format>"
    print "Format options:"
    print "-1 : Firstname Lastname"
    print "-2 : Firstname.Lastname"
    print "-3 : Firstname_Lastname"
    print "-4 : FinitialLastname"


def initialLast(name):
    names = name.split(' ')
    firstName = names[0]
    lastName = names[1]
    firstInitial = firstName[0]
    username = firstInitial + lastName.replace('\n','') + "@" + sys.argv[2]
    return username.lower()


def fullFirstLast(name):
    names = name.split(' ')
    firstName = names[0]
    lastName = names[1]
    username = firstName + lastName.replace('\n','') + "@" + sys.argv[2]
    return username.lower()


def firstDotLast(name):
    names = name.split(' ')
    firstName = names[0]
    lastName = names[1]
    username = firstName + '.' + lastName.replace('\n','') + "@" + sys.argv[2]
    return username.lower()

def firstUnderScoreLast(name):
    names = name.split(' ')
    firstName = names[0]
    lastName = names[1]
    username = firstName + '_' + lastName.replace('\n','') + "@" + sys.argv[2]
    return username.lower()


if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] == "-h":
        helpText()
        sys.exit(0)

    elif sys.argv[3] == '-1':
        print "[*] Generated name list for FirstnameLastname:"
        for line in open(sys.argv[1]):
            print fullFirstLast(line)
            

    elif sys.argv[3] == '-2':
        print "[*] Generated name list for Firstname.Lastname:"
        for line in open(sys.argv[1]):
            print firstDotLast(line)
            

    elif sys.argv[3] == '-3':
        print "[*] Generated name list for Firstname_Lastname:"
        for line in open(sys.argv[1]):
            print firstUnderScoreLast(line)
            

    elif sys.argv[3] == '-4':
        print "[*] Generated name list for FinitialLastname:"
        for line in open(sys.argv[1]):
            print initialLast(line)
            

    else:
        helpText()
        sys.exit(0)
