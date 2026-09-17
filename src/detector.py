
def detect_repeated_failures(parsed_events, threshold = 3):
    ip_counts= {}
    user_counts = {}
    invalid_user_counts = {}
    root_counts = {}
    alerts = []
    for event in parsed_events:
        source_ip = event['source_ip']
        username = event['username']
        event_type = event['event_type']

        if event_type == 'successful_login':
            if username in user_counts and user_counts[username] >= threshold:
                alert = {
                    'alert_type': 'Successful login after repeated failures',
                    'username': username,
                    'source_ip': source_ip,
                    'previous_failures': user_counts[username]
                }

                alerts.append(alert)

            continue

        if source_ip in ip_counts:
            ip_counts[source_ip] += 1
        else:
            ip_counts[source_ip] = 1

        if username in user_counts:
            user_counts[username] += 1
        else:
            user_counts[username] = 1

        if event_type == 'invalid_user_failure':
            if username in invalid_user_counts:
                invalid_user_counts[username] += 1
            else:
                invalid_user_counts[username] = 1

    
        if event_type == 'root_login_failure':
            if username in root_counts:
                root_counts[username] += 1
            else:
                root_counts[username] = 1

    for source_ip, count in ip_counts.items():
        if count >= threshold:
            alert = {
                'alert_type': 'Repeated IP failure',
                'source_ip': source_ip,
                'failed_attempts': count
            }

            alerts.append(alert)

    for username, count in user_counts.items():
        if count >= threshold:
            alert = {
                'alert_type': 'Repeated user failure',
                'username': username,
                'failed_attempts': count
            }

            alerts.append(alert)

    for username, count in invalid_user_counts.items():
        if count >= threshold:
            alert = {
                'alert_type': 'Repeated invalid user failure',
                'username': username,
                'failed_attempts': count
            }

            alerts.append(alert)

    for username, count in root_counts.items():
        if count >= threshold:
            alert = {
                'alert_type': 'Repeated root login failure',
                'username': username,
                'failed_attempts': count
            }

            alerts.append(alert)
    return alerts