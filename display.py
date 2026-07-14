from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import time

console = Console()

def hour_to_12(hour):
    if hour == 0:
        return "12 AM"
    if hour < 12:
        return f"{hour} AM"
    if hour == 12:
        return "12 PM"
    return f"{hour - 12} PM"

def display_wrapped(profile, language_breakdown, analysis, persona):
    # Card 1 — Profile
    join_year = profile["join_date"][:4]
    console.print(Panel(
        f"[bold]{profile['name']}[/bold]\n"
        f"📅 Joined the party in {join_year}\n"
        f"📦 Public repos: {profile['public_repo_count']}\n"
        f"👥 Followers: {profile['followers']}",
        title="👤 PROFILE",
        border_style="magenta"
    ))
    time.sleep(0.8)

    # Card 2 — Activity
    console.print(Panel(
        f"[bold cyan]{analysis['total_commits']}[/bold cyan] total commits\n"
        f"🔥 Most active day: [bold]{analysis['most_active_day']}[/bold]\n"
        f"⏰ Peak hour: [bold]{hour_to_12(analysis['most_active_hour'])}[/bold]\n"
        f"🌙 Late-night commits: {analysis['late_night_count']} ({analysis['late_night_pct']}%)",
        title="📊 YOUR ACTIVITY",
        border_style="cyan"
    ))
    time.sleep(0.8)

    # Card 3 — Languages
    table = Table(title="💻 YOUR LANGUAGES", border_style="green")
    table.add_column("Language", style="bold")
    table.add_column("Share", justify="left")
    for lang, pct in language_breakdown.items():
        bar = "█" * max(1, int(pct / 10))
        table.add_row(lang, f"[green]{bar}[/green] {pct}%")
    console.print(table)
    time.sleep(0.8)

    # Card 4 — Persona (the finale)
    name, description = persona
    console.print(Panel(
        f"[bold magenta]{name}[/bold magenta]\n\n{description}",
        title="🎁 YOUR CODING PERSONA",
        border_style="magenta",
        padding=(1, 2)
    ))