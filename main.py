from fetchers import fetch_user_profile, fetch_repos, fetch_all_commits
from analyzers import calculate_language_breakdown

username = input("Enter a GitHub username: ")

profile = fetch_user_profile(username)
if profile is None:
    print(f"Could not fetch profile for '{username}'.")
    exit()

repos = fetch_repos(username)
if repos is None:
    print(f"Could not fetch repos for '{username}'.")
    exit()

timestamps = fetch_all_commits(username, repos)
if not timestamps:
    print(f"No commits found for '{username}'.")
    exit()

language_breakdown = calculate_language_breakdown(repos)
print(language_breakdown)  # temporary - replaced by display_wrapped soon