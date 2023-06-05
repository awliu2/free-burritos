import asyncio
from twscrape import AccountsPool, API, gather
import time
import config as cfg
import code_handler
import os

# user id of chipotle's twitter account
USER_ID = 141341662

async def main():
    # initialize the account login
    if 'accounts.db' in os.listdir():
        os.remove('accounts.db')
    
    pool = AccountsPool()
    await pool.add_account(cfg.login['username'], cfg.login['password'], 
                            cfg.login['email'], cfg.login['password'])
    await pool.login_all()
    api = API(pool)

    # initialize a code_handler object
    handler = code_handler.CodeHandler()

    # attempt to get the latest tweet from chipotle's twitter account
    while True:
        tweets = await gather(api.user_tweets(USER_ID, limit=1))
        if not tweets:
            print("no tweets found")
            continue

        latest_tweet = tweets[0]
        t_content = latest_tweet.rawContent
        t_time = latest_tweet.date.strftime("%Y-%m-%d %H:%M:%S")
        if not handler.handle_tweet(t_content):
            print(f"failed to handle tweet {t_content[0:60]}... at {t_time}")
        else:
            print(f"successfully handled tweet {t_content[0:60]}... at {t_time}")
        time.sleep(2)
    

if __name__ == "__main__":
    asyncio.run(main())
