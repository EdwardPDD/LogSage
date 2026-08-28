# LogSage

LogSage is a Python based security log analysis tool designed to analyze Linux and Windows system logs and identify security relevant activity. The project focuses on parsing authentication events, extracting useful information, detecting suspicious patterns, and generating readable security reports.

I built LogSage as a hands-on cybersecurity project to develop practical experience with Python, Linux system logs, SSH authentication, virtualized environments, and security event analysis.

## Current Features

- Reads Linux authentication logs line-by-line
- Identifies failed SSH password attempts
- Identifies invalid-user login attempts
- Identifies failed root login attempts
- Identifies sudo authentication failures
- Identifies successful SSH logins
- Handles invalid log file paths using exception handling
- Uses case-insensitive event matching while preserving the original log entries

## Technologies and Environment

- Python 3
- Ubuntu Server
- Windows 11 host system
- VMware Workstation
- Visual Studio Code
- VS Code Remote SSH
- SSH
- Git and GitHub
- Linux authentication logs ('/var/log/auth.log')

LogSage is developed and tested on an Ubuntu Server virtual machine running in VMware Workstation. I connect to the server from my Windows 11 host using SSH and VS Code Remote SSH, allowing the application to run directly within the Linux environment where the system logs are generated.

## Architecture

LogSage is organized into separate modules so that log parsing, threat detection, reporting, and user interaction have their own responsibilities.

- 'main.py' provides the user interface and controls which type of log analysis is performed.
- 'linux_parser.py' reads and classifies Linux log events.
- 'windows_parser.py' will handle Windows Event Logs.
- 'detector.py'' will analyze parsed events for suspicious patterns.
- 'report_generator.py'' will format analysis results into readable security reports.

This separation allows the parser to focus on determining what happened in the logs, while the detector can focus on determining whether the activity may be suspicious.

## Testing

The Linux parser was tested using authentication events generated on the Ubuntu Server VM. From my Windows 11 host, I used PowerShell and SSH to intentionally generate failed and successful authentication events.

I then examined '/var/log/auth.log' using Linux tools such as 'grep'' and compared the actual log entries with the results produced by LogSage. This testing helped identify overly broad matching rules, which were refined to improve the accuracy of event classification.

## Project Status and Roadmap

LogSage is currently under active development. The Linux parser can classify several authentication-related security events, and the next phase will focus on extracting useful information from individual log entries.

Planned development includes:

- Extract usernames, source IP addresses, ports, timestamps, and event types from authentication logs
- Store parsed events in a structured format
- Develop detection rules for suspicious authentication patterns
- Detect repeated failed authentication attempts
- Identify successful logins following repeated failures
- Generate readable security reports
- Add Windows Event Log parsing and analysis
- Expand testing as additional detection features are added

## Development Notes

Detailed development notes documenting the project setup, implementation decisions, testing process, troubleshooting, and lessons learned are available in:

### docs/development-notes.md

The development notes are maintained throughout the project to document how LogSage was built and how problems were identified and resolved during testing.