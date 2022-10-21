import requests
from requests_oauthlib import OAuth1
import json


CLIENT_ID = "mtShmC7sHcVuvlfNNjbHl4or8"
CLIENT_SECRET = "mVDWnkAUEcWe2y8VfC2jdsuHqWezmWsPRwQ5O7s25cW73NF73M"
TOKEN_KEY = "1286219864911122433-dndbqaQBzuW116A9r7uxFLvEa39U3K"
TOKEN_SECRET = "12X83jty6PH7jpGgc6FhUGafRsNmzgAKWivufF49xQGdY"



oauth = OAuth1(CLIENT_ID,
    client_secret=CLIENT_SECRET,
    resource_owner_key=TOKEN_KEY,
    resource_owner_secret=TOKEN_SECRET,
)

response = requests.post(
    "https://api.twitter.com/2/tweets/",
    auth = oauth,
)

