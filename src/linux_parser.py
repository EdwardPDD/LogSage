def extract_username(line):
    normalized_line = line.strip().lower()

    if 'failed password for invalid user' in normalized_line:
        username = normalized_line.split('invalid user')[1].split()[0]
        return username

    if 'failed password for' in normalized_line:
        username = normalized_line.split('failed password for')[1].split()[0]
        return username

    return None

def extract_source_ip(line):
    normalized_line = line.strip().lower()

    if 'failed password' in normalized_line:
        ip_address = normalized_line.split('from')[1].split()[0]
        return ip_address

    return None

def extract_port(line):
    normalized_line = line.strip().lower()

    if 'failed password' in normalized_line:
        port = normalized_line.split(' port ')[1].split()[0]
        return port

    return None

def analyze_linux_logs(): 
    print()
    print('Analyzing Linux Logs...')

    log_path = input('Enter the path to the Linux log file: ')

    failed_events = []
    invalid_user_events = []
    root_login_events = []
    sudo_failure_events = []
    successful_ssh_events = []
    usernames = []
    ip_addresses = []
    ports = []

    try:
        with open (log_path, 'r') as log_file:
           for line in log_file:
                normalized_line = line.strip().lower()

                username = extract_username(line)
                if username is not None:
                    usernames.append(username)

                ip_address = extract_source_ip(line)
                if ip_address is not None:
                    ip_addresses.append(ip_address)

                port = extract_port(line)
                if port is not None:
                    ports.append(port)

                if 'failed password' in normalized_line:
                    failed_events.append(line.strip())

                if 'failed password for invalid user' in normalized_line:
                    invalid_user_events.append(line.strip())

                if 'failed password for root' in normalized_line: 
                    root_login_events.append(line.strip())

                if 'sudo' in normalized_line and 'authentication failure' in normalized_line:
                    sudo_failure_events.append(line.strip())

                if 'accepted password' in normalized_line:
                    successful_ssh_events.append(line.strip())

        print()
        print(f'Total failed login attempts: {len(failed_events)}')
        print(f'Total invalid user login attempts: {len(invalid_user_events)}')
        print(f'Total failed root login attempts: {len(root_login_events)}')
        print(f'Total sudo authentication failures: {len(sudo_failure_events)}')
        print(f'Total successful SSH login attempts: {len(successful_ssh_events)}')
        print(f'Extracted usernames: {usernames}')
        print(f'extracted source IP addresses: {ip_addresses}')
        print(f'Extracted ports: {ports}')

         
    except FileNotFoundError:
        print()
        print('File not found. Please check the path and try again.')