import httpx
import json
import time
import random

class Discord:
    def __init__(self) -> None:
        self.discord_oauth = ""
        self.response = ""
        self.guild_id = 0
        self.channel_id = 0
        self.discord_header = {
            "Authorization": "", # Replace me plz
            "Content-Type": "application/json",
        }
        
        self.proxies = self.load_proxies()

    def load_proxies(self):
        with open('proxies.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]

    def get_random_proxy(self):
        return random.choice(self.proxies)

    def send_discord_payload(self) -> str:
        proxy = self.get_random_proxy()
        proxies = {
            "http://": proxy,
            "https://": proxy,
        }

        self.post_data = json.dumps({
            "authorize": True,
            "guild_id": f"{self.guild_id}",
            "integration_type": 0,
            "permissions": "0"
        })

        oauth_url = "https://discord.com/api/v9/oauth2/authorize?client_id=755827207812677713&response_type=code&scope=rpc.voice.read%20rpc.activities.write%20guilds.members.read%20identify&state="
        self.test = httpx.post(oauth_url, data=self.post_data, follow_redirects=True, headers=self.discord_header)
        json_response = self.test.json()
        location_url = json_response.get('location', '')
        self.discord_oauth = location_url.split("code=")[-1] if "code=" in location_url else ''
        

        callback_url = f"https://755827207812677713.discordsays.com/papi/api/oauth-callback/755827207812677713?code={self.discord_oauth}&channel_id={self.channel_id}&guild_id={self.guild_id}"
        self.response = httpx.get(callback_url, headers=self.discord_header, follow_redirects=False).json()
        
        
        try:
            return (self.response["user"], self.response["token"])
        except Exception:
            reverify_data = json.dumps({
                "guild_id": f"{self.guild_id}",
                "session_id": "263c72a1f43e475327da33aee6fec4cb"
            })
            
            reverify_url = f"https://discord.com/api/v9/activities/{self.channel_id}/755827207812677713"
            test = httpx.post(reverify_url, headers=self.discord_header, data=reverify_data)
            print(test)
            
            oauth_url = "https://discord.com/api/v9/oauth2/authorize?client_id=755827207812677713&response_type=code&scope=rpc.voice.read%20rpc.activities.write%20guilds.members.read%20identify&state="
            self.test = httpx.post(oauth_url, data=self.post_data, follow_redirects=True, headers=self.discord_header)
            json_response = self.test.json()
            location_url = json_response.get('location', '')
            self.discord_oauth = location_url.split("code=")[-1] if "code=" in location_url else ''
            
            
            callback_url = f"https://755827207812677713.discordsays.com/papi/api/oauth-callback/755827207812677713?code={self.discord_oauth}&channel_id={self.channel_id}&guild_id={self.guild_id}"
            self.response = httpx.get(callback_url, headers=self.discord_header, follow_redirects=False).json()
            #print(self.response)
           
            return (self.response["user"], self.response["token"])
        except httpx.RequestError as e:
            print(f"Request failed: {e}. Retrying with a different proxy.")
            self.proxies.remove(proxy)  
            return self.send_discord_payload() 

    def parse_putt_info(self) -> None:
        self.channel_id = input("ChannelID: ")
        self.guild_id = input("GuildID: ")

        while True:
            user_info = self.send_discord_payload()
           
            print(f"Party Token: {user_info[1]['access_token']}.{user_info[1]['refresh_token']}")
            print(f"Userinfo: {user_info[0]}")

if __name__ == "__main__":
    Discord().parse_putt_info()

