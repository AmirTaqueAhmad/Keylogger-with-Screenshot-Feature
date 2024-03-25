**Keylogger with Email Reporting and Screenshot Capture**

This Python script serves as a keylogger with the additional functionality of capturing screenshots and sending reports via email. It can be useful for monitoring user activity on a local machine for various purposes, including security monitoring and parental control.

### Features:
- **Keylogging:** The script logs keystrokes pressed by the user.
- **Screenshot Capture:** It captures screenshots of the desktop.
- **Email Reporting:** The captured keystrokes and screenshots are sent as email attachments to a specified email address.

### Requirements:
- Python 3.x
- Required Python libraries: `smtplib`, `email.mime`, `PIL`, `pynput`

### Usage:
1. Set up email parameters by providing the sender's email address, password, and recipient's email address.
2. Run the script.
3. The script will continuously monitor the user's activity, capturing keystrokes and taking screenshots at regular intervals.
4. Reports containing the keystrokes and screenshots will be sent to the specified email address every minute.

### Note:
- Ensure that you have enabled access for less secure apps in your Gmail account settings if you are using a Gmail account as the sender.
- Use this script responsibly and in compliance with applicable laws and regulations regarding privacy and monitoring.

### Disclaimer:
This script is provided for educational and informational purposes only. The author is not responsible for any misuse or damage caused by the use of this script. Use it at your own risk.

For any issues or suggestions, please feel free to open an issue or pull request on GitHub. Thank you for using our keylogger script!
