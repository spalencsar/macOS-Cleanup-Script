import os
import subprocess
import shutil
import datetime
import smtplib
from email.mime.text import MIMEText

# Function to print colored text
def print_colored_text(color, text):
    print(f"\033[1m\033[{color}m{text}\033[0m")

# Disclaimer and Liability Notice
def print_disclaimer():
    print_colored_text("35", "=================================================")
    print_colored_text("35", "                   DISCLAIMER                    ")
    print_colored_text("35", "=================================================")
    print("")
    print("This script is provided as-is, without any warranty or guarantee.")
    print("The author of this script takes no responsibility for any damage or loss")
    print("caused by the use or misuse of this script.")
    print("")
    print("By using this script, you acknowledge that you are using it at your own risk.")
    print("The author cannot be held liable for any consequences or damages arising from the use of this script.")
    print("")
    print_colored_text("35", "If you agree to these terms and conditions, enter 'yes' to continue executing the script.")
    print("Entering any other value will terminate the script.")
    print("")
    print_colored_text("35", "Beta Build Version: 0.9")
    print_colored_text("35", "Author: Noordjonge")
    print("")
    print_colored_text("35", "=================================================")
    print("")

def get_user_confirmation():
    confirmation = input("Do you agree to the terms and conditions? (yes/no): ").lower()
    return confirmation == "yes"

# Function to create a backup of important files
def create_backup():
    print_colored_text("36", "Creating backup of important files...")
    backup_dir = f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(backup_dir, exist_ok=True)
    
    try:
        shutil.copytree(os.path.expanduser("~"), os.path.join(backup_dir, "home_backup"))
        print_colored_text("32", "Backup created successfully.")
    except Exception as e:
        print_colored_text("31", f"Error creating backup: {e}")
    print("")

# Function to log actions
def log_action(action):
    with open("maintenance_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}: {action}\n")

# Function to check system status
def check_system_status():
    print_colored_text("36", "Checking system status...")
    try:
        subprocess.run(["df", "-h"], check=True)  # Disk space
        subprocess.run(["top", "-l", "0"], check=True)  # CPU usage
    except Exception as e:
        print_colored_text("31", f"Error checking system status: {e}")
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
        print_colored_text("31", f"Error during network diagnostics: {e}")
    print("")

# Function to check for outdated software
def check_outdated_software():
    print_colored_text("36", "Checking for outdated software...")
    try:
        subprocess.run(["softwareupdate", "-l"], check=True)
        print_colored_text("32", "Outdated software check completed.")
    except Exception as e:
        print_colored_text("31", f"Error checking for outdated software: {e}")
    print("")

# Function to delete private data
def delete_private_data():
    print_colored_text("36", "Deleting private data...")
    try:
        # Example: Deleting Safari browsing history and cookies
        shutil.rmtree(os.path.expanduser("~/Library/Safari/"), ignore_errors=True)
        print_colored_text("32", "Private data deleted successfully.")
    except Exception as e:
        print_colored_text("31", f"Error deleting private data: {e}")
    print("")

# Function to analyze disk space and list largest files
def analyze_disk_space():
    print_colored_text("36", "Analyzing disk space...")
    try:
        print_colored_text("33", "Largest files in home directory:")
        subprocess.run("du -ah ~ | sort -rh | head -n 10", shell=True)
        print_colored_text("32", "Disk space analysis completed.")
    except Exception as e:
        print_colored_text("31", f"Error analyzing disk space: {e}")
    print("")

# Function to send email notifications
def send_email_notification(subject, body):
    sender_email = "your_email@example.com"
    receiver_email = "receiver_email@example.com"
    password = "your_password"  # Use an app password if necessary

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        print_colored_text("32", "Email notification sent successfully.")
    except Exception as e:
        print_colored_text("31", f"Error sending email: {e}")

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
        print_colored_text("31", f"Error during security check: {e}")
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
    print_disclaimer()
    
    if get_user_confirmation():
        main_menu()
    else:
        print_colored_text("31", "Script execution aborted. Exiting...")n
