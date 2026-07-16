import datetime
import os
import requests

# GitHub username to query
USER_NAME = "YarooqH"

# Calculate Uptime since Yarooq Anwar started his career (October 2020)
def calculate_uptime():
    start_date = datetime.datetime(2020, 10, 1)
    today = datetime.datetime.today()
    
    # Calculate years and months
    years = today.year - start_date.year
    months = today.month - start_date.month
    days = today.day - start_date.day
    
    if days < 0:
        # Subtract one month, calculate days in previous month
        months -= 1
        # Get last day of previous month
        prev_month = today.replace(day=1) - datetime.timedelta(days=1)
        days += prev_month.day
        
    if months < 0:
        years -= 1
        months += 12
        
    y_str = f"{years} year{'s' if years != 1 else ''}"
    m_str = f"{months} month{'s' if months != 1 else ''}"
    d_str = f"{days} day{'s' if days != 1 else ''}"
    
    return f"{y_str}, {m_str}, {d_str}"

def fetch_stats():
    # Set up auth headers if ACCESS_TOKEN / GITHUB_TOKEN is available
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("ACCESS_TOKEN")
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"
        
    # Default fallback values
    stats = {
        "UPTIME": calculate_uptime(),
        "REPOS": "15+",
        "COMMITS": "2,840+",
        "STARS": "5+",
        "FOLLOWERS": "2"
    }
    
    try:
        # 1. Fetch user data (repos, followers)
        user_url = f"https://api.github.com/users/{USER_NAME}"
        r = requests.get(user_url, headers=headers, timeout=10)
        if r.status_code == 200:
            user_data = r.json()
            stats["REPOS"] = str(user_data.get("public_repos", stats["REPOS"]))
            stats["FOLLOWERS"] = str(user_data.get("followers", stats["FOLLOWERS"]))
            
        # 2. Fetch repo stargazers
        repos_url = f"https://api.github.com/users/{USER_NAME}/repos?per_page=100"
        r_repos = requests.get(repos_url, headers=headers, timeout=10)
        if r_repos.status_code == 200:
            repos_data = r_repos.json()
            stars_sum = sum(repo.get("stargazers_count", 0) for repo in repos_data)
            stats["STARS"] = str(stars_sum)
            
        # 3. Fetch total commits (using search commits API)
        search_commits_url = f"https://api.github.com/search/commits?q=author:{USER_NAME}"
        # Search commits API requires a specific accept header
        commit_headers = headers.copy()
        commit_headers["Accept"] = "application/vnd.github.cloak-preview"
        r_commits = requests.get(search_commits_url, headers=commit_headers, timeout=10)
        if r_commits.status_code == 200:
            stats["COMMITS"] = f"{r_commits.json().get('total_count', stats['COMMITS']):,}"
            
    except Exception as e:
        print(f"Error fetching stats from API: {e}. Using fallback values.")
        
    return stats

def update_svgs():
    stats = fetch_stats()
    print(f"Stats loaded: {stats}")
    
    templates = {
        "neofetch_template_dark.svg": "neofetch_dark.svg",
        "neofetch_template_light.svg": "neofetch_light.svg"
    }
    
    for template_name, output_name in templates.items():
        if os.path.exists(template_name):
            with open(template_name, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Replace all placeholders
            for key, val in stats.items():
                content = content.replace(f"{{{key}}}", val)
                
            with open(output_name, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Generated {output_name} from template.")
        else:
            print(f"Template {template_name} not found!")

if __name__ == "__main__":
    update_svgs()
