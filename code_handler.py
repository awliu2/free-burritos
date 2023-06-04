import re
import os
import pyautogui
import pyperclip
from pynput import mouse


class CodeHandler:
    """
    Implementation of the code handler object.
    This object is responsible for finding promotional codes in tweets,
    and pasting them into the imessage text box. This object also keeps
    track of which codes have already been used, and writes them to disk.
    """

    def __init__(self, use_manual_location=False):
        # create a file to store seen codes if it doesn't exist
        if 'seen_codes.txt' not in os.listdir():
            open('seen_codes.txt', 'w').close()
        
        # load seen codes into memory
        self.seen_codes = set(l.strip() for l in open('seen_codes.txt', 'r'))
        
        self.location = None
        if use_manual_location:
            print("#"*40)
            print("Click on the imessage text box to continue")
            print("#"*40)
            self.location = self.__click_to_get_text_box()
        
        else:
            print("Attempting to locate iMessages text box")
            print("Please make sure that the iMessages window is open")
            while self.location is None:
                try:
                    self.location = self.__get_text_box()
                except:
                    continue
        
        print(f"Text box location: {self.location}")
    
    
    def __find_code(self, content):
        # attempts to find a code in a given string
        pattern1= "FREETHREES.... to 888222"
        pattern2= "BONUSFREEPOINTER.... to 888222"
        match1 = re.search(pattern1, content)
        match2 = re.search(pattern2, content)
        if match1:
            return match1.group().split(" ")[0]
        elif match2:
            return match2.group().split(" ")[0]
        else:
            return None
    
    def __save_code(self, code):
        # saves a given code to disk
        self.seen_codes.add(code)
        with open('seen_codes.txt', 'a') as f:
            f.write(f"{code}\n")
            f.flush()
    
    def __get_text_box(self):
        # function to get location of imessages text box
        for img in ['txtmsg1.png', 'txtmsg2.png']:
            try:
                message_box_loc = pyautogui.locateCenterOnScreen("screenshots/" + img, confidence = 0.9)
                if message_box_loc:
                    print(message_box_loc)
                    return message_box_loc.x // 2, message_box_loc.y // 2
            except:
                continue
            
        
    def __click_to_get_text_box(self):
        # function to get location of imessages text box by clicking on it
        # in case automatic text box location fails
        def on_click(x, y, button, pressed):
            if pressed:
                return False
            
        listener = mouse.Listener(on_click=on_click)
        listener.start()
        listener.join()

        x, y = pyautogui.position()
        return x, y

    
    def __paste_code(self, location, code):
        # paste a given code into the imessage text box
        pyperclip.copy(code)
        x, y = location
        pyautogui.moveTo(x, y)
        pyautogui.click()
        pyautogui.click()
        pyautogui.hotkey('command', 'v')
        pyautogui.press('enter')

    
    def handle_tweet(self, tweet_content):
        # outward facing function to handle a given promotional code
        code = self.__find_code(tweet_content)
        
        if not code:
            return False
        
        if code in self.seen_codes:
            print(f"Code {code} already used")
            return False
        
        else:
            self.__save_code(code)
            self.__paste_code(self.location, code)
            return True
    
    # outward facing function to update the text box location
    def update_location(self):
        self.location = self.__get_text_box()
    