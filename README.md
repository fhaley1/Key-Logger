# Disclaimer
This tool is for educational purposes only, this author does not endorse or promote any illegal activity and is not responsible for any damage done henceforth.

I also highly recommend only testing this out using fake email addresses, and not personal email accounts

# Key-Logger
A keylogger is a type of software or hardware that records every keystroke you type on a keyboard. It's often used to secretly capture sensitive information like passwords or messages.

# What is Keylogger ?
The action of recording (logging) the keys struck on a keyboard, often discreetly, so that the person using the keyboard is unaware that their activities are being observed. The person who is running the key logging program can then obtain the data. Keylogger is most often used to steal passwords and other confidential information.

# What does this Keylogger do?
This Keylogger when activated, will: 
- Run in the background of the victims session 
- Record every keystroke the victim types
- Record information about the victims computer, such as their operating system, CPU, IP address, etc
- Record information saved to their clipboard (what the copy/paste)
- Take screenshots of their screen

Once this information is gathered for a specified amount of time (this can be for as long as you like), the information will be encrypted and sent back to the user via encrypted files. These encrypted files can then be decrypted using the DecryptFile.py script.

This Key Logger will also delete the information gathered on the victims computer, so they will never know their activty was recorded in the first place.

# How to get this Keylogger to work:
Ensure you have the following pips/modules installed:
- pywin32
- pynput
- cryptography
- requests
- pillow
- scipy

For this key logger to work, you must do the following:

- Set the file path you wish to save the gathered information to , an example has been provided in the script
  
- Generate an encrpytion key using GenerateEncryptionKey.py , an example has been provided
  
- Copy paste the encryption key saved to the encryption_key.txt file into the 'key' variable in AdvancedKeyLogger.py and DecryptFile.py , an example encryption key has been provided

- Have Two-Factor-Authentication (2FA) enabled on your Gmail account

- Have or generate an 'App Password'. To do this: go to 'Manage your Google Account', 'Security', 'App Passwords'

- Generate an 'App Password' and save it somewhere safe as you will not be able to access this password again.

- Paste your generated password into the password variable, you should be able to send emails via python.

# Disclaimer
This tool is for educational purposes only!

Gmail somtimes prevents sending certain files for security reasons. If you encounter this problem, I suggest using Yahoo mail instead as I never encountered issues when testing this out on Yahoo email addresses.

If you use Yahoo email addresses you will have to change the following under 'Sending Email Function':
- smtp_server = "smtp.mail.yahoo.com"
- smtp_port = # 587 should work, but try port 465 if 587 does not work


