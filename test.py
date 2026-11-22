
from pynput import mouse
import pyautogui
import subprocess
import time


selected = []

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        selected.append((int(x), int(y)))
        return False

print("Click the pixel you want to select.")

with mouse.Listener(on_click=on_click) as listener:
    listener.join()

x, y = selected[0]
print("Selected position:", x, y)



#

was_red = False

while True:
    #r, g, b = pyautogui.pixel(x, y)
    screenshot = pyautogui.screenshot()
    r, g, b = screenshot.getpixel((x * 2, y * 2))[:3]

    is_red = r == 226 and g == 116 and b == 102
    
    if is_red and not was_red:
    
            print("ALERT: Status turned red!")
    
            subprocess.run([
    
                "osascript",
    
                "-e",
    
                'display notification "Red status detected" with title "NOC Monitor"'
    
            ])
            

    

    if not is_red and was_red:
        print("Status is no longer red.")
        was_red = False

    was_red = is_red



# keyboard.wait('space')
##print(pyautogui.position())
# print(pyautogui.pixel(420, 420))
# if pyautogui.pixel(420, 420) == (69, 66, 65):
#     print("Red pixel detected!")