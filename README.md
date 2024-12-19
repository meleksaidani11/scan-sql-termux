# SQL Injection Vulnerability Scanner

## Description
This is a simple SQL Injection vulnerability scanner designed for ethical hacking purposes. The tool uses a provided SQL Dork to search for potentially vulnerable websites and tests them for SQL Injection vulnerabilities. It is specifically designed to run on Termux or any terminal-based Python environment.

## Features
- Dork-based website search using Google.
- SQL Injection vulnerability testing for found websites.
- Interactive terminal-based interface with `curses`.
- Developed with simplicity and usability in mind.

## Installation
Follow these steps to install and run the tool on Termux:

1. **Install Python**  
   Install Python if not already installed:
   ```bash
   pkg install python


Install the necessary Python libraries:


1. **Install Python**  
   Install Python if not already installed:
   ```bash
   pip install requests beautifulsoup4 curses
   
Usage
Run the script:

python scan.py
Enter the required inputs:

SQL Dork: A search query to find websites.
Number of Pages: Number of Google search result pages to scan.
View results directly in the terminal interface:

Vulnerable websites will be marked as [+] Vulnerable.
Non-vulnerable websites will be marked as [-] Not Vulnerable.
Notes
The tool is designed for educational and ethical purposes only. Do not use it to target websites without explicit permission.
Google may block multiple requests if made in a short period. Use the tool responsibly.
Disclaimer
This tool is for educational purposes only. The developer is not responsible for any misuse or illegal activity involving this tool.

Developer
Developed by Melek Saidani
