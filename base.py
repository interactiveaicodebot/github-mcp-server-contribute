import requests

class GitHubInsightsAPI:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.github.com"
        self.proxies = {
            "http": "http://70.10.15.10:8080",
            "https": "http://70.10.15.10:8080"
        }

    def get_repo_insights(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/stats/contributors"
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        response = requests.get(url, headers=headers, proxies=self.proxies, verify=False)
        return response.json()

    def get_commit_activity(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/stats/commit_activity"
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        response = requests.get(url, headers=headers, proxies=self.proxies, verify=False)
        return response.json()

    def get_code_frequency(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/stats/code_frequency"
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        response = requests.get(url, headers=headers, proxies=self.proxies, verify=False)
        return response.json()

if __name__ == "__main__":
    # Example usage
    token = "YOUR_GITHUB_TOKEN"  # Replace with your actual GitHub token
    api = GitHubInsightsAPI(token)

    owner = "octocat"
    repo = "Hello-World"

    print("Repository Insights:")
    print(api.get_repo_insights(owner, repo))

    print("\nCommit Activity:")
    print(api.get_commit_activity(owner, repo))

    print("\nCode Frequency:")
    print(api.get_code_frequency(owner, repo))