from linux_parser import analyze_linux_logs 

def display_banner(): 
    print('===================================')
    print('        LogSage Security Tool      ')
    print('===================================')


def display_menu():
    print('1. Analyze Linux Logs')
    print('2. Analyze Windows Logs')
    print('3. Exit')


def main():
    while True:
        display_banner()
        display_menu()

        choice = input('select an option: ')


        if choice == '1':
            analyze_linux_logs()

        elif choice == '2':
            print()
            print('Analyzing Windows Logs...')
            

        elif choice == '3':
            print()
            print('Exiting the program...')
            break
            

        else:
            print()
            print('Invalid option. Please try again.')
            


if __name__ == '__main__':
    main()