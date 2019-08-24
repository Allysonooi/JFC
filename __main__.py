import sys
import os
import random
filename = 'dict.txt'

def read():
    if os.path.exists(filename):
        if os.path.getsize(filename) == 0:
            print "My goodness. Why are you reading an empty file?!"
            print "Go to the ADD mode! BYE."
        else:
            file = open(filename,"r")
            for line in file.readlines():
                str = line.split(', ')
                print str[0]
                print str[1]
            file.close()
    else :
        print "The file does NOT exist."
        print "Either this is your first time.. Or you lost your file."
        print "I shall be a kind soul to help you to create the file..."
        print "Creation in progress..."
        file = open(filename,"w")
        file.close()

    print "=============== C O M P L E T E ======================"

def search(japString, engMeaning):
    file = open(filename,"r")
    for line in file.readlines():
        str = line.split(', ')
        if japString == '' or engMeaning == '':
            if japString == str[0] or engMeaning == str[1].rstrip():
                return [str[0], str[1].rstrip()]
        else :
            if japString == str[0] or engMeaning == str[1].rstrip():
                return True
    return False

def add_vocab(japString, engMeaning):
    file = open(filename,"a")
    file.write(japString + ', ' + engMeaning)
    file.write('\n')
    file.close()

def del_vocab(japString, engMeaning):
    del_line = japString + ', ' + engMeaning
    with open(filename, "r") as file:
        lines = file.readlines()
    with open(filename, "w") as file:
        for line in lines:
            if line.strip("\n") != del_line:
                file.write(line)
    file.close()

def edit_vocab(japString, engMeaning):
    del_vocab(japString, engMeaning)
    japString_NEW = raw_input("Input NEW Japanese String: ")
    engMeaning_NEW = raw_input("Input NEW English Meaning: ")
    add_vocab(japString_NEW, engMeaning_NEW)

def test_vocab():
    while True:
        file = open(filename,"r")
        lines = file.readlines()
        str = random.choice(lines).split(', ')
        num = random.randint(0, 1)
        if num == 0 :
            print "Japanese String: " + str[0]
            answer = raw_input("Input English Meaning: ")

            if answer == 'q':
                print "Tiring to continue ehs? Alright, rest well and try later!"
                break
            elif answer == str[1].rstrip():
                print "\nCORRECT!\n"
            else:
                print "\nINCORRECT!"
                print "Actual Answer: " + str[0].rstrip() + '\n'


def main():
    while True :
        action = raw_input('\nPlease input an option. \n' +
                            '1 - Read Dictionary\n' +
                            '2 - Search for Vocab\n' +
                            '3 - Add new Vocab\n' +
                            '4 - Edit Vocab\n' +
                            '5 - Delete Vocab\n' +
                            '6 - Test yourself\n' +
                            '7 - To Quit\n\n')

        if action == '1':
            print "\n================= R E A D ===================="
            read()
        elif action == '2':
            print "\n================== S E A R C H ==================="
            while True:
                print "Instructions: \nInput either Japanese String or English Meaning, leave the other empty.\n"
                japString = raw_input("Input Japanese String: ")
                engMeaning = raw_input("Input English Meaning: ")
                if japString == '' and engMeaning == '':
                    print "Empty input. Do you even really want to search ?"
                else:
                    check = search(japString, engMeaning)
                    print "\nSearch Results :"
                    if check == True :
                        print japString
                        print engMeaning
                    elif check == False :
                        print "Nothing found."
                    else :
                        print check[0]
                        print check[1]
                print "=============== C O M P L E T E ======================"

                cont = raw_input("Do you want to continue the SEARCH mode? [Y/N]\n")
                if cont == 'Y' or cont == 'y' or cont == 'yes':
                    continue
                elif cont == 'N' or cont == 'n' or cont == 'no' :
                    break
                else:
                    print 'I am going bring you to the menu since you are unable to make up your mind.'
                    print 'BYE.'
                    break

        elif action == '3':
            print "\n================== A D D ==================="
            while True:
                print "Instructions: \nInput both Japanese String and English Meaning.\n"
                japString = raw_input("Input Japanese String: ")
                engMeaning = raw_input("Input English Meaning: ")
                if japString == '' or engMeaning == '':
                    print "Empty input. Do you even really want to add a new one?"
                else:
                    if search(japString, engMeaning) == True :
                        print "This vocab already exists... You should already know this ._. Try again!"
                    else :
                        add_vocab(japString, engMeaning)

                print "=============== C O M P L E T E ======================"
                cont = raw_input("Do you want to continue the ADD mode? [Y/N]\n")
                if cont == 'Y' or cont == 'y' or cont == 'yes':
                    continue
                elif cont == 'N' or cont == 'n' or cont == 'no' :
                    break
                else:
                    print 'I am going bring you to the menu since you are unable to make up your mind.'
                    print 'BYE.'
                    break

        elif action == '4':
            print "\n================== E D I T ==================="
            while True:
                print "Instructions: \nInput either Japanese String or English Meaning, leave the other empty.\n"
                japString = raw_input("To edit Japanese String: ")
                engMeaning = raw_input("To edit English Meaning: ")
                if japString == '' and engMeaning == '':
                    print "Empty input. Do you even really want to search ?"
                else:
                    check = search(japString, engMeaning)
                    print "\nSearch Results :"
                    if check == True :
                        print japString
                        print engMeaning
                        edit_vocab(japString, engMeaning)
                    elif check == False :
                        print "Does Not Exist!"

                    else :
                        print check[0]
                        print check[1]
                        edit_vocab(check[0], check[1])

                print "\n=============== C O M P L E T E ======================"

                cont = raw_input("Do you want to continue the EDIT mode? [Y/N]\n")
                if cont == 'Y' or cont == 'y' or cont == 'yes':
                    continue
                elif cont == 'N' or cont == 'n' or cont == 'no' :
                    break
                else:
                    print 'I am going bring you to the menu since you are unable to make up your mind.'
                    print 'BYE.'
                    break

        elif action == '5':
            print "\n================== D E L E T E ==================="
            while True:
                print "Instructions: \nInput either Japanese String or English Meaning, leave the other empty.\n"
                japString = raw_input("Input Japanese String: ")
                engMeaning = raw_input("Input English Meaning: ")
                if japString == '' and engMeaning == '':
                    print "Empty input. Do you even really want to search ?"
                else:
                    check = search(japString, engMeaning)
                    print "\nSearch Results :"
                    if check == True :
                        print japString
                        print engMeaning
                        del_vocab(japString, engMeaning)
                    elif check == False :
                        print "Does Not Exist!"

                    else :
                        print check[0]
                        print check[1]
                        del_vocab(check[0], check[1])

                print "\n=============== C O M P L E T E ======================"

                cont = raw_input("Do you want to continue the DELETE mode? [Y/N]\n")
                if cont == 'Y' or cont == 'y' or cont == 'yes':
                    continue
                elif cont == 'N' or cont == 'n' or cont == 'no' :
                    break
                else:
                    print 'I am going bring you to the menu since you are unable to make up your mind.'
                    print 'BYE.'
                    break

        elif action == '6':
            print "\n================== T E S T ==================="
            test_vocab()

        elif action == '7':
            print "\n================= Q U I T ===================="
            print "Done with training? Goodbye then!\n"
            sys.exit()

        else :
            print "\n====================================="
            print "Invalid Option."
            print "Sigh. Program will be exiting now because you are incapable of selecting the options.."
            print "OR you are using a Non English keyboard to type the number.."
            print "Try again when your IQ increases. See ya.\n"
            sys.exit()

if __name__== "__main__":
  main()
