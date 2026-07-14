from datetime import datetime, timezone, timedelta
from statistics import mode

def calculate_language_breakdown(repos):
    if not repos:
        return {}
    total = len(repos)
    language_dict = {}
    for repo in repos:
        if repo["language"] not in language_dict:
            language_dict[repo["language"]] = 1
        else:
            language_dict[repo["language"]] += 1
    for lang in language_dict:
        percent = (language_dict[lang]/total) * 100
        language_dict[lang] = round(percent, 1)
    sorted_language_dict = dict(sorted(language_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_language_dict

def analyze_commit_times(timestamps):
    if not timestamps:
        return None
    local_tz = timezone(timedelta(hours=4), name="GST")
    commit_hours = []
    commit_days = []
    total_commits = len(timestamps)
    late_night_count = 0
    for ts in timestamps:
        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        local_dt = dt.astimezone(local_tz)
        commit_hour = local_dt.hour
        commit_hours.append(commit_hour)
        commit_day = local_dt.strftime("%A")
        commit_days.append(commit_day)
        if commit_hour >= 23 or commit_hour <= 3:
            late_night_count += 1

    commit_analysis = {
        "total_commits": total_commits,
        "most_active_hour": mode(commit_hours),
        "most_active_day": mode(commit_days),
        "late_night_count": late_night_count,
        "late_night_pct": round((late_night_count / total_commits) * 100, 1)
    }
    return commit_analysis

def determine_persona(analysis, language_breakdown):
    if analysis["late_night_pct"] >= 40:
        return ("The Midnight Mechanic", f"{analysis['late_night_pct']}% of your commits happen after 11 PM. Your best ideas happen in the dark, and honestly, your weirdest bugs do too.")
    if analysis["most_active_hour"] >= 5 and analysis["most_active_hour"] <= 8:
        return ("The Early Bird", "Committing code before the sun—and most developers' first cup of coffee—is even up. Terrifying efficiency; your team loves you, but they also fear you.")
    if analysis["most_active_day"] in ("Saturday", "Sunday"):
        return ("The Weekend Warrior", "While others were touching grass, you were pushing code. For you, the weekend isn’t a break—it's just uninterrupted side-project time.")
    for lang in language_breakdown:
        if language_breakdown[lang] >= 70:
            return ("The Purist", "You are fiercely loyal to a single language. Everyone else is chasing shiny new frameworks, but you’ve committed to one syntax for better or for worse—mostly for worse.")
    if len(language_breakdown) > 4:
        return ("The Polyglot", "You're running a full-blown coding circus. You refuse to settle down with one stack, choosing instead to collect languages like infinity stones just to see what happens.")
    return ("The Ghost Committer", "You slip in, drop some solid code, and vanish without a trace. No weird midnight habits, no weekend binges—just clean, mysterious execution.")