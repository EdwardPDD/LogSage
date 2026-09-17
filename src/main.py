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
            print()
            print('=== Security Alerts ===')

            for alert in security_alerts:
                print()

                print(f"Alert Type: {alert['alert_type']}")

                if 'username' in alert:
                    print(f"Username: {alert['username']}")

                if 'source_ip' in alert:
                    print(f"Source IP: {alert['source_ip']}")

                if 'failed_attempts' in alert:
                    print(f"Failed Attempts: {alert['failed_attempts']}")

                if 'previous_failures' in alert:
                    print(f"Previous Failures: {alert['previous_failures']}") 


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