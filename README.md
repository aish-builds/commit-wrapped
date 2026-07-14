# Commit Wrapped 🎁

Your GitHub activity, Spotify Wrapped style. A Python CLI tool that analyzes any 
GitHub user's public activity and generates a personalized "Wrapped" — commit 
stats, language breakdown, and a coding persona — displayed as animated 
terminal cards.

## Features
- Fetches any GitHub user's profile, repositories, and commit history via the 
  GitHub REST API
- Analyzes commit timestamps (converted to local time, GST) to find your most 
  active day, peak coding hour, and late-night commit percentage
- Calculates your language breakdown across all public repos
- Assigns you one of six coding personas based on your habits — from 
  The Midnight Mechanic to The Ghost Committer
- Wrapped-style card reveal in the terminal using rich (colors, panels, 
  progress bars, staged timing)
- Authenticated requests via personal access token (5,000 req/hour) with 
  secure .env handling

## Tech Stack
- Python 3.13
- requests — GitHub REST API calls
- rich — terminal UI (panels, tables, styling)
- python-dotenv — environment variable management

## How to Run
1. Clone the repo
```bash
   git clone git@github.com:aish-builds/commit-wrapped.git
   cd commit-wrapped
```
2. Install dependencies
```bash
   pip3 install requests rich python-dotenv
```
3. (Optional but recommended) Create a GitHub personal access token with the 
   `public_repo` scope, then create a `.env` file in the project root:
   GITHUB_TOKEN=your_token_here
   Without a token, requests are limited to 60/hour.
4. Run it
```bash
   python3 main.py
```
   Enter any GitHub username when prompted.

## Project Structure
commit-wrapped/
├── main.py        # Orchestrates the pipeline: fetch → analyze → display
├── fetchers.py    # GitHub API calls (profile, repos, commits)
├── analyzers.py   # Language breakdown, commit-time analysis, persona logic
└── display.py     # rich terminal cards

## Known Limitations
- **100-commit cap per repo** — no pagination yet, so very active repos are 
  undercounted
- **Languages measured by repo count, not bytes** — a 10-line HTML repo weighs 
  the same as a 5,000-line Python repo
- **Public repos only** — private activity requires OAuth (planned for Phase 3)
- **Forked repos** — only commits authored by the user are counted, but fork 
  languages still appear in the breakdown
- **Recent repos only, capped at 100** — users with 100+ repositories get a 
  partial picture
- **Hardcoded timezone (GST/UTC+4)** — late-night stats assume the user is in 
  Dubai; other timezones get skewed persona results
- **Sequential API calls** — one request per repo means users with many repos 
  wait noticeably (the N+1 problem; async requests or GraphQL would fix this)
- **No caching** — every run refetches everything from the GitHub API

## Roadmap
- **Phase 1 (this version):** CLI with heuristic personas ✅
- **Phase 2:** Web app — Next.js, Tailwind, Framer Motion card animations, 
  Claude API for dynamic AI-generated personas, deployed on Vercel
- **Phase 3:** GitHub OAuth for private repo data, shareable Wrapped cards

## What I Learned
- Working with a real REST API end to end: endpoints, query parameters 
  (`?author=` to filter fork noise, `?per_page=100`), status codes, and 
  rate limits (hit the 60/hour anonymous cap mid-development)
- Secure credential handling: tokens in .env, .gitignore verification before 
  every push, minimal-scope permissions
- Timezone conversion with datetime, timezone, and timedelta — commit 
  timestamps arrive in UTC and needed converting to GST for accurate 
  late-night stats
- Modular architecture: separating fetching, analysis, and display means 
  Phase 2 can replace the display layer entirely while the analyzers survive 
  untouched
- Hidden complexity analysis: refactored a language counter from O(n²) 
  (list membership checks) to O(n) (dict lookups)
- The N+1 API problem — fetching commits requires one request per repo, 
  which is exactly the pain GraphQL exists to solve

## Author
Aishwarya Kumaran — [GitHub](https://github.com/aish-builds)
