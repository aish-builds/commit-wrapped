from fetchers import fetch_user_profile, fetch_repos, fetch_all_commits
from analyzers import calculate_language_breakdown, analyze_commit_times, determine_persona
from display import hour_to_12, display_wrapped

username = input("Enter GitHub username: ")

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
analysis = analyze_commit_times(timestamps)
persona = determine_persona(analysis, language_breakdown)

display_wrapped(profile, language_breakdown, analysis, persona)