import pyautogui

print(pyautogui.size())
def get_text_box():
    while True:
        try:
            message_box_loc = pyautogui.locateCenterOnScreen('txtmsg.png', confidence = 0.9)
            if message_box_loc:
                return message_box_loc.x // 2, message_box_loc.y // 2
        except:
            continue



def paste_code(location):
    x, y = location
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.click()
    pyautogui.hotkey('command', 'v')
    # pyautogui.press('enter')


paste_code(get_text_box())