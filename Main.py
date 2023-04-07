from colorama import init, Fore, Style
init()
import random
from pprint import pprint



with open('words.txt', 'r') as f:
    Words = [line.strip() for line in f]

turn = 1

answer = random.choice(Words)
answercap = answer.capitalize()
answerLetter = ([*answercap])


while turn < 7:

    inputWord = input("Word? ")
    inputcap = inputWord.capitalize()
    inputLetter = ([*inputcap])
   
    if len(inputWord) == 5:

        if inputLetter[0] in answerLetter:

            if inputLetter[0] == answerLetter [0]:
                print(Fore.GREEN + str(inputLetter[0]), end="")
                print(Style.RESET_ALL, end="")
            else:
                print(Fore.YELLOW + str(inputLetter[0]), end="")
                print(Style.RESET_ALL, end="")
        else:
            print(Fore.WHITE + str(inputLetter[0]), end="")
            print(Style.RESET_ALL, end="")

        if inputLetter[1] in answerLetter:

            if inputLetter[1] == answerLetter [1]:
                print(Fore.GREEN + str(inputLetter[1]), end="")
                print(Style.RESET_ALL, end="")
            else:
                print(Fore.YELLOW + str(inputLetter[1]), end="")
                print(Style.RESET_ALL, end="")
        else:
            print(Fore.WHITE + str(inputLetter[1]), end="")
            print(Style.RESET_ALL, end="")

        if inputLetter[2] in answerLetter:

            if inputLetter[2] == answerLetter [2]:
                print(Fore.GREEN + str(inputLetter[2]), end="")
                print(Style.RESET_ALL, end="")
            else:
                print(Fore.YELLOW + str(inputLetter[2]), end="")
                print(Style.RESET_ALL, end="")
        else:
            print(Fore.WHITE + str(inputLetter[2]), end="")
            print(Style.RESET_ALL, end="")

        if inputLetter[3] in answerLetter:

            if inputLetter[3] == answerLetter [3]:
                print(Fore.GREEN + str(inputLetter[3]), end="")
                print(Style.RESET_ALL, end="")
            else:
                print(Fore.YELLOW + str(inputLetter[3]), end="")
                print(Style.RESET_ALL, end="")
        else:
            print(Fore.WHITE + str(inputLetter[3]), end="")
            print(Style.RESET_ALL, end="")

        if inputLetter[4] in answerLetter:

            if inputLetter[4] == answerLetter [4]:
                print(Fore.GREEN + str(inputLetter[4]), end="")
                print(Style.RESET_ALL)
            else:
                print(Fore.YELLOW + str(inputLetter[4]), end="")
                print(Style.RESET_ALL)
        else:
            print(Fore.WHITE + str(inputLetter[4]), end="")
            print(Style.RESET_ALL)
        
        if inputLetter == answerLetter:
            if turn == 1:
                print(Fore.CYAN + "YOU WON ON YOUR FIRST TRY!")
            else:
                print(Fore.CYAN + "YOU TOOK " + str(turn) + " TRIES TO GET IT!")
                y = input("Press Enter To Close")
            print(Style.RESET_ALL)
            exit()
        if turn == 6:
            pprint("YOU LOST THE WORD WAS: " + answer)
            x = input("Press Enter To Close")

        turn = turn + 1


    else:
        print(Fore.RED + 'THE WORD THAT YOU CHOOSE IS NOT 5 CHARTERS LONG')
        print(Style.RESET_ALL)
        exit()



