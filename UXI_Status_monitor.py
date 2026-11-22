#from pynput import mouse
import mouse
import time
import subprocess
import keyboard 
import pyautogui

print("Click the pixel you want to monitor...")

# Wait until you left-click somewhere

# def on_click(x, y, button, pressed):
#
#     if pressed and button == mouse.Button.left:
#
#         return False  # Stop listening
#
# with mouse.Listener(on_click=on_click) as listener:
#
#     listener.join()\\
x, y = "hi"
keyboard.wa
if keyboard.is_pressed('o'):
    x, y = pyautogui.position()
# Get the selected pixel coordinates


print(f"Monitoring pixel at ({x}, {y})")

was_red = False

while True:
     # Read the pixel color

    r, g, b = pyautogui.pixel(x, y)

    # Check whether the pixel is red

    is_red = r > 150 and r > g + 25 and r > b + 25

    print(f"RGB: {r}, {g}, {b} | Red: {is_red}")

    # Notify only when the status changes to red

    if is_red and not was_red:

        print("ALERT: Status turned red!")

        subprocess.run([

            "osascript",

            "-e",

            'display notification "Red status detected" with title "NOC Monitor"'

        ])

    
    

    was_red = is_red

    # if was_red and not is_red:
    #     print("Status recovered. now green")
    #     subprocess.run([
    #
    #         "osascript",
    #
    #         "-e",
    #
    #         'display notification "Status recovered" with title "NOC Monitor"'
    #
    #     ])



    time.sleep(5)




##was_red = False
