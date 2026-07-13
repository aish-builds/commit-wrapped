import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
headers = {"Authorization": f"token {TOKEN}"}

username = "aish-builds"
response = requests.get(f"https://api.github.com/users/{username}/repos", headers=headers)
repos = response.json() 
#parses response from JSON format to python objects (list of nested dictionaries)

for repo in repos:
    print(repo["name"], "—", repo["language"])