import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
headers = {"Authorization": f"token {TOKEN}"}

def fetch_user_profile(username):
    response = requests.get(f"https://api.github.com/users/{username}", headers=headers)

    if response.status_code != 200:
        return None
    
    data = response.json()
    return {
        "name": data["name"] or data["login"],
        "join_date": data["created_at"],
        "public_repo_count": data["public_repos"],
        "followers": data["followers"]
        }

def fetch_repos(username):
    response = requests.get(f"https://api.github.com/users/{username}/repos?per_page=100", headers=headers)
    
    if response.status_code != 200:
        return None
    
    repos = response.json()
    all_repos = []
    for repo in repos:
        data = {
            "name": repo["name"],
            "language": repo["language"] or "Other",
            "stars": repo["stargazers_count"],
            "created_date": repo["created_at"]
            }
        all_repos.append(data)
    return all_repos


def fetch_all_commits(username, repos):
    timestamps = []
    for repo in repos:
        response = requests.get(f"https://api.github.com/repos/{username}/{repo['name']}/commits?author={username}&per_page=100", headers=headers)

        if response.status_code != 200:
            continue
        
        commits = response.json()
        for commit in commits:
            timestamps.append(commit["commit"]["author"]["date"])
    return timestamps
