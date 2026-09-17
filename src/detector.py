
def detect_repeated_failures(parsed_events, threshold = 3):
    ip_counts= {}
    alerts = []
    for event in parsed_events:
        source_ip = event['source_ip']

        if source_ip in ip_counts:
            ip_counts[source_ip] += 1
        else:
            ip_counts[source_ip] = 1


    for source_ip, count in ip_counts.items():
        if count >= threshold:
            alert = {
                'source_ip': source_ip,
                'failed_attempts': count
            }

            alerts.append(alert)

    return alerts