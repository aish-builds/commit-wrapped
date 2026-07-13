from fetchers import fetch_user_profile, fetch_repos

username = "aish-builds"

profile = fetch_user_profile(username)

if profile is None:
    print(f"Could not fetch profile for {username}.")
else:
    print(profile)

repos = fetch_repos(username)

if repos is None:
    print(f"Could not fetch the repos for {username}.")
else:
    print(repos)