# 🌯 Burrito Bot
A bot to get the three-pointer promo codes during the 2023 NBA finals.

## Install & Requirements

* Python 3.10+
* Mac with iMessages enabled
* Text Message forwarding enabled
* valid twitter account

### Install
```
git clone https://github.com/awliu2/free-burritos.git
cd free-burritos
pip3 install -r requirements.txt
```

or `pip`, whichever one works for you.


## Setup

1. First, create a `config.py` file in the same directory, and fill it in as follows, replacing the credentials with a valid twitter account. 

    ```
    login = {
        "email" : "john@gmail.com",
        "username" : "johnstwitter",
        "password" : "password123",
    }
    ```

2. Next, make sure you have text message forwarding enabled: [instructions here.](https://support.apple.com/en-us/HT208386)

## Usage
Open iMessages, and start a new message with the Chipotle short code number (888222), make sure that it is on the top of your window, and run:
```
python3 burrito_bot.py
```
The script will attempt to automatically detect the iMessage window location. Ensure that the iMessage window remains visible when running the script.

### Automatic vs Manual text box detection

If automatic detection doesn't work (depending on screen resolution, display scaling), use manual text box detection instead.
```
python3 burrito_bot.py -m
```

When prompted, click on the iMessage text box, making sure to click **inside the oval**: 
![iMessage text box](screenshots/messagebox.png)


### Notes

* The twitter API has a 250 request per 15 minutes per account limit. Thus, if the script does not seem to be working, but it is able to locate the imessage window, the API request is likely timing out. (250 seconds / 2 seconds per request $\approx$ 8.3 minutes of continuous runtime before timing out).

* Since this bot requires cursor and keyboard access, it is best not to use your machine at the same time.

* credit to [baolong281](https://github.com/baolong281/infinite-food-glitch) for the general idea of this project.



