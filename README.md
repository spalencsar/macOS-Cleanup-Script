# ⚠️ ARCHIVED PROJECT - DO NOT USE ⚠️

# macOS Cleanup Script (DEPRECATED)

> **🚨 CRITICAL WARNING: This script is OBSOLETE and potentially DANGEROUS on modern macOS systems!**
> 
> **📅 Last Update:** 2025 - Project archived  
> **⛔ Status:** No longer maintained - DO NOT USE  
> **🎯 Target:** macOS versions prior to macOS 12 (now unsupported)

## ⚠️ Why This Script is Dangerous

This script contains **outdated and potentially harmful commands** that can:
- **Break your macOS system** (uses deprecated `diskutil verifyPermissions`)
- **Delete critical user data** without proper safeguards
- **Compromise system security** with aggressive modifications
- **Interfere with modern macOS features** like SIP and automatic maintenance

## 🏛️ Historical Context

This script was created for older macOS versions (pre-2020) when manual system maintenance was more common. Modern macOS handles most of these tasks automatically and securely.

## ✅ Modern Alternatives (2025)

Instead of this script, use:
- **Built-in macOS maintenance** (runs automatically)
- **Storage Management** (Apple Menu > About This Mac > More Info > Storage Settings)
- **CleanMyMac X** or **OnyX** for advanced cleanup
- **Time Machine** for proper backups
- **Terminal maintenance commands** individually and carefully

## Author
Sebastian Palencsar

Version: 1.0 (FINAL - ARCHIVED)

## Overview (Historical)

~~This script performs various maintenance tasks on a macOS system, including creating backups, checking system status, performing network diagnostics, and more.~~

**Note:** These functions are now handled by macOS automatically or available through safer, modern tools.

## Disclaimer and Liability Notice

This script is provided as-is, without any warranty or guarantee. The author of this script takes no responsibility for any damage or loss caused by the use or misuse of this script.

By using this script, you acknowledge that you are using it at your own risk. The author cannot be held liable for any consequences or damages arising from the use of this script.

This script is intended for educational and informational purposes only. It is recommended to review and understand the code before executing it.

By using this script, you agree to the terms and conditions stated above.

## Prerequisites

- macOS version 12.7 or higher
- Python 3 must be installed.

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    ```
2. **Navigate to the directory**:
    ```bash
    cd macOS-Cleanup-Script
    ```
3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Python Installation

If Python 3 is not installed, you can install it as follows:

1. **Download the Python installer** from the official [Python website](https://www.python.org/downloads/).
2. **Run the installer** and follow the instructions to install Python 3.

## Configuration

1. **Create a `.env` file** and add your email credentials:
    ```plaintext
    EMAIL_PASSWORD=your_password
    ```
    This file is used to store sensitive information like your email password securely.

2. **Edit the `config.ini` file** to store custom settings:
    ```ini
    [EMAIL]
    SENDER_EMAIL = your_email@example.com
    RECEIVER_EMAIL = receiver_email@example.com
    SMTP_SERVER = smtp.example.com
    SMTP_PORT = 587

    [BACKUP]
    BACKUP_DIR = /path/to/backup
    ```
    This file is used to configure email settings and the backup directory.

## Running the Script

1. **Clone or download this repository** to your local machine.

2. **Open a terminal** and navigate to the directory containing the script.

3. **Run the script** using the following command:
   ```bash
   python3 system_maintenance_script.py
   ```

4. **Follow the on-screen instructions** to choose the desired maintenance tasks from the main menu.

## Example Usage

Here is an example of how to use the script:

```bash
# Run the script
python3 system_maintenance_script.py

# Select an option from the menu
1. Create Backup
2. Analyze Disk Space
3. Network Diagnostics
4. Exit
```

## Features

- Create backup of important files
- Clean system cache
- Empty trash
- Check disk permissions
- Renew Spotlight index
- Clear DNS cache
- Change DNS server
- Run Internet speedtest
- Delete private data
- Analyze disk space
- Check for outdated software
- Display system information
- Check system status
- Perform network diagnostics
- Check for software updates
- Perform security check
- Send email notifications
- Error logging and notifications

## Contributing

If you encounter issues, have suggestions, or want to contribute to the script's development, please feel free to open an issue or submit a pull request on the 

[GitHub repository](https://github.com/noordjonge/macOS-Cleanup-Script).

## License

This project is licensed under the MIT License.
