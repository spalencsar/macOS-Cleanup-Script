#!/usr/bin/env python3
"""
⚠️  ARCHIVED PROJECT - DO NOT USE ⚠️

macOS Cleanup Script (DEPRECATED)
Author: Sebastian Palencsár
Version: 1.0 (FINAL - ARCHIVED)
Status: OBSOLETE - DO NOT RUN ON MODERN macOS

🚨 CRITICAL WARNING: 
This script is DANGEROUS on modern macOS systems!
- Contains deprecated commands that can break your system
- Uses unsafe practices that can cause data loss
- Not compatible with modern macOS security features

This script is kept for historical reference only.
Use modern alternatives instead!
"""

import os
import subprocess
import shutil
import datetime
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import logging
import configparser
import sys

# Check if Python is installed
def check_python_installation():
    try:
        subprocess.run(["python3", "--version"], check=True)
    except subprocess.CalledProcessError:
        print("Python is not installed. Please install Python 3 to run this script.")
        sys.exit(1)

# Load environment variables from .env file
load_dotenv()

# Load configuration from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Configure logging
logging.basicConfig(filename='maintenance_log.txt', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Function to print colored text
def print_colored_text(color, text):
    print(f"\033[1m\033[{color}m{text}\033[0m")

# Function to install speedtest-cli if not already installed
def install_speedtest_cli():
    try:
        import speedtest
    except ImportError:
        print_colored_text("36", "Installing speedtest-cli...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "speedtest-cli"])
        print_colored_text("32", "speedtest-cli installed successfully.")

# Function to send error notifications
def send_error_notification(error_message):
    subject = "Error in macOS Cleanup Script"
    body = f"An error occurred during the execution of the macOS Cleanup Script:\n\n{error_message}"
    send_email_notification(subject, body)

# Disclaimer and Liability Notice
def print_disclaimer():
    print_colored_text("31", "=================================================")
    print_colored_text("31", "   ⚠️  ARCHIVED PROJECT - DO NOT USE ⚠️   ")
    print_colored_text("31", "=================================================")
    print("")
    print_colored_text("31", "🚨 CRITICAL WARNING: This script is OBSOLETE!")
    print("")
    print("This script contains DANGEROUS and DEPRECATED commands that can:")
    print("• BREAK your macOS system (uses removed diskutil commands)")
    print("• DELETE critical user data without proper safeguards")
    print("• COMPROMISE system security")
    print("• INTERFERE with modern macOS features")
    print("")
    print_colored_text("31", "DO NOT RUN THIS SCRIPT ON MODERN macOS!")
    print("")
    print("This script is provided as-is, without any warranty or guarantee.")
    print("The author of this script takes no responsibility for any damage or loss")
    print("caused by the use or misuse of this script.")
    print("")
    print("By using this script, you acknowledge that you are using it at your own risk.")
    print("The author cannot be held liable for any consequences or damages arising from the use of this script.")
    print("")
    print("This script is intended for educational and historical purposes only.")
    print("It is recommended to use modern macOS tools instead.")
    print("")
    print("By using this script, you agree to the terms and conditions stated above.")
    print("")
    print_colored_text("31", "⚠️  This script should NOT be used - type 'archive' to acknowledge")
    print("Entering any other value will terminate the script.")
    print("")
    print_colored_text("35", "Build Version: 1.0 (FINAL - ARCHIVED)")
    print_colored_text("35", "Author: Sebastian Palencsár")
    print("")
    print_colored_text("31", "=================================================")
    print("")

def get_user_confirmation():
    confirmation = input("Type 'archive' to acknowledge this script is obsolete: ").lower()
    if confirmation == "archive":
        print_colored_text("31", "\n⚠️  You have acknowledged this script is obsolete.")
        print_colored_text("31", "The script will now exit for your safety.")
        print_colored_text("32", "\nRecommended alternatives:")
        print("• Use built-in macOS Storage Management")
        print("• Try CleanMyMac X or OnyX for cleanup")
        print("• Use Time Machine for backups")
        return False
    else:
        return False

# Function to create a backup of important files
def create_backup():
    print_colored_text("36", "Creating backup of important files...")
    backup_dir = config['BACKUP']['BACKUP_DIR']
    os.makedirs(backup_dir, exist_ok=True)
    
    try:
        shutil.copytree(os.path.expanduser("~"), os.path.join(backup_dir, f"home_backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"))
        print_colored_text("32", "Backup created successfully.")
    except Exception as e:
        error_message = f"Error creating backup: {e}"
        print_colored_text("31", error_message)
        logging.error(error_message)
        send_error_notification(error_message)
    print("")

# Function to log actions
def log_action(action):
    logging.info(action)

# Function to check system status
def check_system_status():
    print_colored_text("36", "Checking system status...")
    try:
        subprocess.run(["df", "-h"], check=True)  # Disk space
        subprocess.run(["top", "-l", "0"], check=True)  # CPU usage
    except Exception as e:
        error_message = f"Error checking system status: {e}"
        print_colored_text("31", error_message)
        logging.error(error_message)
        send_error_notification(error_message)
    print("")

# Function to perform network diagnostics
def network_diagnostics():
    print_colored_text("36", "Performing network diagnostics...")
    try:
        print_colored_text("33", "Pinging Google...")
        subprocess.run(["ping", "-c", "4", "google.com"], check=True)
        
        print_colored_text("33", "Running traceroute...")
        subprocess.run(["traceroute", "google.com"], check=True)
        
        print_colored_text("32", "Network diagnostics completed successfully.")
    except Exception as e:
        error_message = f"Error during network diagnostics: {e}"
        print_colored_text("31", error_message)
        logging.error(error_message)
        send_error_notification(error_message)
    print("")

# Function to check for outdated software
def check_outdated_software():
    print_colored_text("36", "Checking for outdated software...")
    try:
        subprocess.run(["softwareupdate", "--list"], check=True)
        print_colored_text("32", "Outdated software check completed.")
    except Exception as e:
        error_message = f"Error checking for outdated software: {e}"
        print_colored_text("31", error_message)
        logging.error(error_message)
        send_error_notification(error_message)
    print("")

# Function to delete private data
def delete_private_data():
    print_colored_text("36", "Deleting private data...")
    try:
        # Example: Deleting Safari browsing history and cookies
        shutil.rmtree(os.path.expanduser("~/Library/Safari/"), ignore_errors=True)
        print_colored_text("32", "Private data deleted successfully.")
    except Exception as e:
        error_message = f"Error deleting private data: {e}"
        print_colored_text("31", error_message)
        logging.error(error_message)
        send_error_notification(error_message)
    print("")

# Function to analyze disk space and list largest files
def analyze_disk_space():
    print_colored_text("36", "Analyzing disk space...")
    try:
        print_colored_text("33", "Largest files in home directory:")
        subprocess.run("du -ah ~ | sort -rh | head -n 10", shell=True)
        print_colored_text("32", "Disk space analysis completed.")
    except Exception as e:
        error_message = f"Error analyzing disk space: {e}"
        print_colored_text("31", error_message)
        logging.error(error_message)
        send_error_notification(error_message)
    print("")

# Function to send email notifications
def send_email_notification(subject, body):
    sender_email = config['EMAIL']['SENDER_EMAIL']
    receiver_email = config['EMAIL']['RECEIVER_EMAIL']
    smtp_server = config['EMAIL']['SMTP_SERVER']
    smtp_port = config['EMAIL']['SMTP_PORT']
    password = os.getenv("EMAIL_PASSWORD")

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        print_colored_text("32", "Email notification sent successfully.")
    except Exception as e:
        error_message = f"Error sending email: {e}"
        print_colored_text("31", error_message)
        logging.error(error_message)

# Function to perform security check
def security_check():
    print_colored_text("36", "Performing security check...")
    try:
        # Check for outdated software
        outdated = subprocess.run(["softwareupdate", "--list"], capture_output=True, text=True)
        if "No new software available" in outdated.stdout:
            print_colored_text("32", "No outdated software found.")
        else:
            print_colored_text("31", "Outdated software detected:")
            print(outdated.stdout)

        # Check for firewall status
        firewall_status = subprocess.run(["/usr/bin/default", "read", "/Library/Preferences/com.apple.alf.plist", "globalstate"], capture_output=True, text=True)
        if "1" in firewall_status.stdout:
            print_colored_text("32", "Firewall is enabled.")
        else:
            print_colored_text("31", "Firewall is disabled.")

    except Exception as e:
        error_message = f"Error during security check: {e}"
        print_colored_text("31", error_message)
        logging.error(error_message)
        send_error_notification(error_message)
    print("")

# Function to clean system cache
def clean_system_cache():
    print_colored_text("36", "Cleaning system cache...")
    try:
        subprocess.run(["sudo", "purge"], check=True)
        print_colored_text("32", "System cache cleaned successfully.")
    except Exception as e:
        error_message = f"Error cleaning system cache: {e}"
        print_colored_text("31", error_message)
        logging.error(error_message)
        send_error_notification(error_message)
    print("")

# Function to empty trash
def empty_trash():
    print_colored_text("36", "Emptying trash...")
    try:
        subprocess.run(["rm", "-rf", os.path.expanduser("~/.Trash/*")], check=True)
        print_colored_text("32", "Trash emptied successfully.")
    except Exception as e:
        error_message = f"Error emptying trash: {e}"
        print_colored_text("31", error_message)
        logging.error(error_message)
        send_error_notification(error_message)
    print("")

# Function to check disk permissions
def check_disk_permissions():
    print_colored_text("36", "Checking disk permissions...")
    try:
        subprocess.run(["diskutil", "verifyPermissions", "/"], check=True)
        print_colored_text("32", "Disk permissions checked successfully.")
    except Exception as e:
        error_message = f"Error checking disk permissions: {e}"
        print_colored_text("31", error_message)
        logging.error(error_message)
        send_error_notification(error_message)
    print("")

# Function to renew Spotlight index
def renew_spotlight_index():
    print_colored_text("36", "Renewing Spotlight index...")
    try:
        subprocess.run(["sudo", "mdutil", "-E", "/"], check=True)
        print_colored_text("32", "Spotlight index renewed successfully.")
    except Exception as e:
        error_message = f"Error renewing Spotlight index: {e}"
        print_colored_text("31", error_message)
        logging.error(error_message)
        send_error_notification(error_message)
    print("")

# Function to clear DNS cache
def clear_dns_cache():
    print_colored_text("36", "Clearing DNS cache...")
    try:
        subprocess.run(["sudo", "killall", "-HUP", "mDNSResponder"], check=True)
        print_colored_text("32", "DNS cache cleared successfully.")
    except Exception as e:
        error_message = f"Error clearing DNS cache: {e}"
        print_colored_text("31", error_message)
        logging.error(error_message)
        send_error_notification(error_message)
    print("")

# Function to change DNS server
def change_dns_server():
    print_colored_text("36", "Changing DNS server...")
    try:
        subprocess.run(["networksetup", "-setdnsservers", "Wi-Fi", "8.8.8.8", "8.8.4.4"], check=True)
        print_colored_text("32", "DNS server changed successfully.")
    except Exception as e:
        error_message = f"Error changing DNS server: {e}"
        print_colored_text("31", error_message)
        logging.error(error_message)
        send_error_notification(error_message)
    print("")

# Function to run Internet speedtest
def run_speedtest():
    print_colored_text("36", "Running Internet speedtest...")
    try:
        import speedtest
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        results = st.results.dict()
        print_colored_text("32", f"Download speed: {results['download'] / 1_000_000:.2f} Mbps")
        print_colored_text("32", f"Upload speed: {results['upload'] / 1_000_000:.2f} Mbps")
        print_colored_text("32", f"Ping: {results['ping']} ms")
    except Exception as e:
        error_message = f"Error running Internet speedtest: {e}"
        print_colored_text("31", error_message)
        logging.error(error_message)
        send_error_notification(error_message)
    print("")

# Function to display system information
def display_system_information():
    print_colored_text("36", "Displaying system information...")
    try:
        subprocess.run(["system_profiler", "SPHardwareDataType"], check=True)
        print_colored_text("32", "System information displayed successfully.")
    except Exception as e:
        error_message = f"Error displaying system information: {e}"
        print_colored_text("31", error_message)
        logging.error(error_message)
        send_error_notification(error_message)
    print("")

# Function to check for software updates
def check_for_updates():
    print_colored_text("36", "Checking for software updates...")
    try:
        subprocess.run(["softwareupdate", "-l"], check=True)
        print_colored_text("32", "Software updates check completed.")
    except Exception as e:
        error_message = f"Error checking for software updates: {e}"
        print_colored_text("31", error_message)
        logging.error(error_message)
        send_error_notification(error_message)
    print("")

# Main menu
def main_menu():
    while True:
        print_colored_text("33", "==================== MAIN MENU ====================")
        print("Please select an option:")
        print("1. Create backup of important files")
        print("2. Clean system cache")
        print("3. Empty trash")
        print("4. Check disk permissions")
        print("5. Renew Spotlight index")
        print("6. Clear DNS cache")
        print("7. Change DNS server")
        print("8. Run Internet speedtest")
        print("9. Delete private data")
        print("10. Analyze disk space")
        print("11. Check for outdated software")
        print("12. Display system information")
        print("13. Check system status")
        print("14. Perform network diagnostics")
        print("15. Check for software updates")
        print("16. Perform security check")
        print("17. Exit")
        print("")

        choice = input("Enter your choice (1-17): ")
        print("")

        if choice == "1":
            create_backup()
            log_action("Backup created.")
            send_email_notification("Backup Created", "A backup of important files has been created.")
        elif choice == "2":
            clean_system_cache()
            log_action("System cache cleaned.")
        elif choice == "3":
            empty_trash()
            log_action("Trash emptied.")
        elif choice == "4":
            check_disk_permissions()
            log_action("Disk permissions checked.")
        elif choice == "5":
            renew_spotlight_index()
            log_action("Spotlight index renewed.")
        elif choice == "6":
            clear_dns_cache()
            log_action("DNS cache cleared.")
        elif choice == "7":
            change_dns_server()
            log_action("DNS server changed.")
        elif choice == "8":
            install_speedtest_cli()
            run_speedtest()
            log_action("Internet speedtest run.")
        elif choice == "9":
            delete_private_data()
            log_action("Private data deleted.")
        elif choice == "10":
            analyze_disk_space()
            log_action("Disk space analyzed.")
        elif choice == "11":
            check_outdated_software()
            log_action("Checked for outdated software.")
        elif choice == "12":
            display_system_information()
            log_action("Displayed system information.")
        elif choice == "13":
            check_system_status()
            log_action("Checked system status.")
        elif choice == "14":
            network_diagnostics()
            log_action("Network diagnostics performed.")
        elif choice == "15":
            check_for_updates()
            log_action("Checked for software updates.")
        elif choice == "16":
            security_check()
            log_action("Performed security check.")
        elif choice == "17":
            print_colored_text("32", "Exiting...")
            break
        else:
            print_colored_text("31", "Invalid choice. Please select a valid option.")

        input("Press Enter to return to the main menu.\n")
        print("")

# Main program
if __name__ == "__main__":
    check_python_installation()
    print_disclaimer()
    
    if get_user_confirmation():
        main_menu()
    else:
        print_colored_text("31", "Script execution aborted. Exiting...")
