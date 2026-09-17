from linux_parser import analyze_linux_logs 
from detector import detect_repeated_failures
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
            security_events = analyze_linux_logs()
            security_alerts = detect_repeated_failures(security_events) 
            print(security_alerts)  

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