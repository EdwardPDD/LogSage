# LogSage Development Notes 

## Project Purpose 

LogSage is a security focused log analysis tool that I am developing in python to analyze Linux and Windows logs. The goal of the project is to identify security authentication events, organize the information into useful categories, detect suspicious patterns, and eventually generate security reports. 

I designed the poject as a hands on way to strenghten my Python, Linux, windows, git, and cybersecurity skills. Rather than working only with simple data, I am testing the Linux portion of LogSage against authentication events generate on my own Ubuntu Server virtual machine. 

The application is being separated into components for log parsing, threat detection, and report generation. This allows each part of the program to have a specific responsibility and makes the project easier to expand and maintain. 

## Development Environment

I built the Linux development and testing environment using A Ubuntu Server virtual machine running in VMware workstation on a windows 11 host. Using a virtual machine gives me an isolated environment where I can generate authentication events, work with Linux system logs, and test LogSage without affecting my main computer. 

I configured SSH access to the Ubuntu server and connected to it remotely through Visual Studio Code using the Remote SSH extension. This allowed VS code  to run on my computer while the project files,python interpreter, terminal commands, and log files remain on the Linux virtual machine. 

The LogSage Git repository is stored on the Ubuntu Server. I use git from the intergrated VS code terminal to trach the changes and push commits to Github. This setup gives me experience working with a remote Linux development environment while maintaining version control. 

## LogSage Structure

I organized LoSage into separa Python modules so that parsing, detection, reporting, and the user interface can be developed independenly. This separation makes the code easier to understand,expand,  test and maintain as additional log sources are added. 

The 'src/main.py' file serves as the entry point for the application. It displays the LogSage menu, accepts the user's selection, and calls the appropriate log analysis function.

The 'src/linux_parser.py' module handles reading and parsing Linux log files. The Linux parser currently focuses on authentication-related events from '/var/log/auth.log'.

The 'src/windows_parser' module is reserved for Windows Event Log parsing. Windows support will be developed after the Linux parsing and detection workflow is established.

The 'src/detector.py' module will contain threat-detection logic. Keeping detection separate from parsing allows the parser to answer what happened in a log while the detector determines whether a pattern of events may represent suspicious activity.

The 'src/report_generator.py' module will eventually format analysis results into readable security reports. Additional directories are used for testing, documentation, sample logs, and generated reports.

## Linux Authentication Parser

I began the Linux parser by allowing the user to provide the path to a Linux log file. The parser uses Python's 'with open()' context manager to safely open the file and processes it line by line instead of loading the entire log into memory. this approach is better suited for log files that may be large.

I added exception handling with 'try' and 'except FileNotFoundError' so that incorrect file paths do not cause the application to terminate with ah unhandled exception. instead, LogSage displays a clear error message and returns control to the application. 

For event matching, each log entry is converted into a normalized lowercase version using 'line.strip().lower()'. The normalized version is used for case insensitive comparisons, while the original log entry stays unchanged when stored. This allows LogSage to simplify event detection without modifying the original log evidence. 

The Linux Parser currently classifies failed SSH password attempts, invalid-user login attempts, failed root login attempts, sudo authentication failures, and successful SSH logins. Matching events are stored in separate Python lists, and 'len()' is used to calculate the number of events in each category. 

## Testing and Troubleshooting 

I tested the parser against real authentication events in '/var/log/auth.log' on the Ubuntu Server VM. From my Windows host I used PowerShell and SSh to connect to the Ubuntu server with intentionally invalid usernames and the root account. this allowed me to generate controlled failed SSH authentication events and then examine how Ubuntu recorded those events in the authentication log. 

I also generated a sudo authentication failure by intentionally entering an incorrect password on the Ubuntu server. Normall SSH connections were used to verify that the parser could also identify successful authentication events. 

During testing I discovered that searching for the word 'failed' was too broad. A single authentication attempt could produce multiple ralted PAM and SSH log messages containing that word, which led to LogSage reporting inflated failure counts. 

I analyzed the actual authentication log using Linux tools such as grep and refined the parser to match more specific messages including 'failed password', 'failed passwrod for invalid user', and 'failed password for root'. After refining the rules, testing confirmed that the parser accurately reported the proper number of authentication events for each category.

## Current Status and Next Steps

The Linux authentication parser can currently identify and categorize several security-relevant authentication events from Ubuntu authentication logs. The current implementation provides the foundation for more detailed security analysis.

The next development phase will focus on extracting useful information from individual log entries, such as usernames, source IP addresses, ports, timestamps, and event types. This information will be stored in a structured format so that events can be compared and analyzed more effectively.

Once event information is structured, the detection module will be developed to identify suspicious patterns such as repeated authentication failures from the same source or successful logins following multiple failed attempts.