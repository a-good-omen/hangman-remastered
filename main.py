import helper

def main():
    helper.Printer("""
                        ╔╗─╔╗╔═══╗╔═╗─╔╗╔═══╗╔═╗╔═╗╔═══╗╔═╗─╔╗
                        ║║─║║║╔═╗║║║╚╗║║║╔═╗║║║╚╝║║║╔═╗║║║╚╗║║
                        ║╚═╝║║║─║║║╔╗╚╝║║║─╚╝║╔╗╔╗║║║─║║║╔╗╚╝║
                        ║╔═╗║║╚═╝║║║╚╗║║║║╔═╗║║║║║║║╚═╝║║║╚╗║║
                        ║║─║║║╔═╗║║║─║║║║╚╩═║║║║║║║║╔═╗║║║─║║║
                        ╚╝─╚╝╚╝─╚╝╚╝─╚═╝╚═══╝╚╝╚╝╚╝╚╝─╚╝╚╝─╚═╝

                            ---------Created By Imu$ak----------""",delay=0.0005)

    input(helper.Printer('\n\n\t\t\t\t  ↲ Press ENTER to start',delay=0.05,clear=False))

    helper.LoginSetup()

    helper.Printer("Loading",dots=4,repetitions=1,delay=0.05)

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
    if choice=='1':
         pass
    elif choice=='2':
         pass
    elif choice=='3':
         pass
    elif choice=='4':
         pass

main()