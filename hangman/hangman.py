import random

def main_menu():
    # Main menu function
    while True:
        try:
            usr_play = str(input('Type "play" to play the game, "exit" to quit:'))
            if usr_play == 'play':
                game()
            elif usr_play == 'exit':
                break
        except:
            pass

def game():
    # game function
    topics_list = ['python', 'java', 'kotlin', 'javascript']
    word_selection = list(random.choice(topics_list))
    word_hidden = list('-' * len(word_selection))
    counter = 8
    char_list = []
    allowed = "abcdefghijklmnopqrstuvwxyz"

    print("H A N G M A N")

    while counter > 0:
        print("")
        print("".join(word_hidden))
        character = input("Input a letter: ")

        if len(character) > 1:
            print("You should input a single letter")
            continue

        if character not in allowed:
            print("It is not an ASCII lowercase letter")
            continue

        if character in word_selection:
            if character in char_list:
                print("You already typed this letter")
            else:
                for i in range(len(word_selection)):
                    if word_selection[i] == character:
                        word_hidden[i] = character
                char_list.append(character)
        else:
            if character in char_list:
                print("You already typed this letter")
            else:
                print("No such letter in the word")
                char_list.append(character)
                counter -= 1

        if word_selection == word_hidden:
            print("")
            print("".join(word_hidden))
            print("You guessed the word!")
            print("You survived!")
            print("")
            break

        if counter == 0:
            print("You are hanged!")
            print("")

# Main routine
main_menu()
