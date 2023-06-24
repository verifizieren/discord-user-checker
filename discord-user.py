import requests
import string
import random
import os
import time
from dotenv import load_dotenv

load_dotenv()

class DiscordUsernameChecker:
    def __init__(self, auth_token):
        self.auth_token = auth_token
    
    def check_user(self, username):
        req = requests.post(
            "https://discord.com/api/v9/users/@me/pomelo-attempt", 
            json={"username": username}, 
            headers={"authorization": self.auth_token}
        )
        
        if req.content == b'{"taken": false}' and req.status_code == 200:
            return 0xA, req
        elif req.content == b'{"taken": true}' and req.status_code == 200:
            return 0xB, req
        else:
            return 0xC, req
    
    @staticmethod
    def generate_random_username(length):
        chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + "._"
        return ''.join(random.choice(chars) for _ in range(length))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Prompt user for input
user_len = int(input("Enter username length: "))
user_delay = int(input("Enter delay (ms): "))
auth_token = os.getenv("TOKEN")
clear_screen()

# Initialize the DiscordUsernameChecker object
username_checker = DiscordUsernameChecker(auth_token)

while True:
    username = username_checker.generate_random_username(user_len)
    check, req = username_checker.check_user(username=username)
    
    if check == 0xA: 
        print(f"✅ {username} is available!")
    elif check == 0xB: 
        print(f"❌ {username} is not available.")
    elif check == 0xC: 
        retry_after = req.json().get('retry_after', 'unknown')
        print(f"⚠️ Failed, Retry in: {retry_after}")
    
    # Only sleep if we actually tried to check a username
    if check in (0xA, 0xB, 0xC):
        time.sleep(user_delay / 1000)
