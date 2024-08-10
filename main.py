import helper

def main():
        helper.ClearScreen()
        input(helper.Printer("""
                        ╔╗─╔╗╔═══╗╔═╗─╔╗╔═══╗╔═╗╔═╗╔═══╗╔═╗─╔╗
                        ║║─║║║╔═╗║║║╚╗║║║╔═╗║║║╚╝║║║╔═╗║║║╚╗║║
                        ║╚═╝║║║─║║║╔╗╚╝║║║─╚╝║╔╗╔╗║║║─║║║╔╗╚╝║
                        ║╔═╗║║╚═╝║║║╚╗║║║║╔═╗║║║║║║║╚═╝║║║╚╗║║
                        ║║─║║║╔═╗║║║─║║║║╚╩═║║║║║║║║╔═╗║║║─║║║
                        ╚╝─╚╝╚╝─╚╝╚╝─╚═╝╚═══╝╚╝╚╝╚╝╚╝─╚╝╚╝─╚═╝

                            ---------Created By Imu$ak----------

                                  ↲ Press ENTER to start""",delay=0.005))

        helper.ClearScreen()
        helper.LoginSetup()
        helper.ClearScreen()

        helper.Loader()
        helper.ClearScreen()

        choice=input(helper.Printer("""
                 ##   ##  ######   ##  ##   ##  ##
                 ### ###  ##       ### ##   ##  ##
                 #######  ##       ######   ##  ##
                 ## # ##  ####     ######   ##  ##
                 ##   ##  ##       ## ###   ##  ##
                 ##   ##  ##       ##  ##   ##  ##
                 ##   ##  ######   ##  ##    ####

                1. Play Game                      _________
                                                           |
                2. Game Help                               0
                                                          /|\\
                3. View Profile                           / \\
                                                 ______________
                4. Exit
        """,delay=0.005))
        helper.ClearScreen()
        if choice=='1':
                pass
        elif choice=='2':
                pass
        elif choice=='3':
                helper.Printer("""
**THE HANGMAN'S CURSE**

In the late 1600s, a secluded village was haunted by a sinister figure known only as the Hangman. The legend\n told of a dark, cursed parchment that appeared in the hands of those who crossed the Hangman’s path. The parchment bore a hidden word that must be\n guessed to escape.

For each incorrect guess, a spectral figure of the Hangman would draw closer to completion—a noose tightening\n around a ghostly neck. The cursed villagers who failed to guess the word were seized by the Hangman, their souls trapped within the parchment’s\n dark embrace.

Though the Hangman disappeared centuries ago, whispers of his curse persist. Those who find the cursed\n parchment or hear the chilling challenge are said to risk becoming the Hangman’s next victims, forever bound to the terror of his eternal game.""",delay=0.05)

main()