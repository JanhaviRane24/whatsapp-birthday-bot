import pyautogui
import keyboard
import time
import os

# Open WhatsApp Desktop (Microsoft Store version)
os.system("start whatsapp:")
time.sleep(5)  # Give time for app to open

 # Use pyautogui.position() to find the contact name and message box position in x and y coordinates
#Eg : position = pyautogui.position()
#print("Current mouse position:", position)

# Start searching for the contact
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)
pyautogui.write("You")#write contact name in your whatsapp
time.sleep(1)
pyautogui.click(x=450, y=307)  # Replace with your contact's name position
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

pyautogui.click(x=809, y=973)# Replace with your message text box position
time.sleep(1)
pyautogui.press('enter')

# Type the message
pyautogui.write("Wish you Happy birthday")
time.sleep(1)

#  Use `keyboard.send` to press Enter (should work even if `pyautogui.press('enter')` does not)
keyboard.send("enter")

print(" Message sent!")
