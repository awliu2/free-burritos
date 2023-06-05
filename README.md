# 🌯 Burrito Bot
### A bot to automate the chipotle three-pointer promo codes during the 2023 NBA finals. Built using [twscrape](https://github.com/vladkens/twscrape), [pyautogui](https://pypi.org/project/PyAutoGUI/), and [pyperclip](https://github.com/asweigart/pyperclip).

___
## Install & Requirements

* Python 3.10+
* Mac with iMessages enabled
* Text Message forwarding enabled
* valid twitter account
___
### Install
```
git clone https://github.com/awliu2/free-burritos.git
cd free-burritos
pip3 install -r requirements.txt
```

or `pip`, whichever one works for you.
___
## Setup

1. Ensure you have python3.10+ [latest version here](https://www.python.org/downloads/). 

2. Update pip:
    ```
    pip3 install --upgrade pip
    ```

3. Make sure to install all dependencies with 
    ```
    pip3 install -r requirements.txt
    ```

4. Navigate to the `free-burritos` directory. Update the contents of `config.py` with the credentials of a valid twitter account. 

    ```
    login = {
        "email" : "john@gmail.com",
        "username" : "johnstwitter",
        "password" : "password123",
    }
    ```

5. Make sure you have text message forwarding enabled for your iMessages account: [instructions here.](https://support.apple.com/en-us/HT208386)

6. The first time you run the script, you may be prompted to grant terminal accessibility access. Do so in system preferences, or else the script will not be able to input mouse and keystrokes.
___
## Usage
Open iMessages, and start a new message with the Chipotle short code number (888222), make sure that it is on the top of your window, and run:
```
python3 burrito_bot.py
```

When prompted, click on the iMessage text box, making sure to click **inside the oval**: 
![iMessage text box](screenshots/messagebox.png)

Ensure that the imessage text box remains fully visible while running the bot. To exit at any time use `ctrl + c`.

___
## Automatic vs Manual text box detection

There is an automatic iMessage window detection mode, which may or may not work as it is reliant on image recognition. You can enable it via the `-a` flag:
```
python3 burrito_bot.py -a
```
The script will attempt to automatically detect the iMessage window location. Ensure that the iMessage window remains visible once you run the script.
(Tested on Macbook Pro 14").

___
## Notes

* The twitter API has a 250 request per 15 minutes per account limit. Thus, if the script does not seem to be working, but it is able to locate the imessage window, the API request is likely timing out. (250 seconds / 2 seconds per request $\approx$ 8.3 minutes of continuous runtime before timing out).

* Since this bot requires cursor and keyboard access, it is best not to use your machine at the same time.

* credit to [baolong281](https://github.com/baolong281/infinite-food-glitch) for the general idea of this project.





